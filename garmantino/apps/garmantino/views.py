# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Category, Item, Image, Property, ItemOnHomePage
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import View
from .services.pack_in_rows import PackInRows
from .services.services import add_categories_to_context
from itertools import chain, cycle


class IndexView(View):
    @staticmethod
    def add_navigation(context):
        context['navigation'] = [{'name': 'Главная', 'url': reverse('index')}]

    @staticmethod
    def get_data_from_db():
        items_on_homepage = ItemOnHomePage.objects.order_by('position')
        items = [obj.item for obj in items_on_homepage]
        items_photos = [item.image_set.first() for item in items]

        items_positions = [obj.position for obj in items_on_homepage]
        photos_urls = [photo.photo.url if photo else settings.DEFAULT_PHOTO_URL for photo in items_photos]
        items_ids = [item.id for item in items]

        return items_positions, photos_urls, items_ids

    @staticmethod
    def get(request):
        items_positions, photos_urls, items_ids = IndexView.get_data_from_db()

        rows = PackInRows.pack_in_rows_by_position([4, 5],
                                                   [pos - 1 for pos in items_positions],
                                                   ['item_id', items_ids],
                                                   ['item_photo_url', photos_urls])
        context = {'rows': rows}

        add_categories_to_context(context)
        return render(request, 'index.html', context)


class CatalogueView(View):
    @staticmethod
    def add_navigation(context):
        IndexView.add_navigation(context)
        context['navigation'] += [{'name': 'Каталог', 'url': reverse('catalogue')}]

    @staticmethod
    def get_data_from_db():
        super_category = Category.objects.get(parent_category_id__isnull=True)
        categories = Category.objects.filter(parent_category_id=super_category.id).order_by('position')
        categories_positions = [category.position - 1 for category in categories]
        categories_ids = [category.id for category in categories]
        categories_names = [category.name for category in categories]
        categories_photos = [category.photo.url for category in categories]

        return categories_positions, categories_ids, categories_names, categories_photos

    @staticmethod
    def get(request):
        positions, ids, names, photos = CatalogueView.get_data_from_db()

        rows = PackInRows.pack_in_rows_by_position(chain([3], cycle([4, 5])),
                                                   positions,
                                                   ['name', names], ['id', ids], ['photo', photos])

        context = {'rows': rows}
        CatalogueView.add_navigation(context)
        add_categories_to_context(context)
        return render(request, 'catalogue_categories.html', context)


class CategoryView(View):
    @staticmethod
    def add_navigation(context, category_id, category_name):
        CatalogueView.add_navigation(context)

        super_category = Category.objects.get(parent_category_id__isnull=True)
        parent_category = Category.objects.get(subcategories=category_id)

        while parent_category.id != super_category.id:
            parent_id = parent_category.id
            context['navigation'] += [{'name': parent_category.name, 'url': reverse('category', args=[parent_id, ])}]
            parent_category = Category.objects.get(subcategories=parent_id)

        context['navigation'] += [{'name': category_name, 'url': reverse('category', args=[category_id, ])}]

    @staticmethod
    def get_items_data_from_db(category_id):
        items = Item.objects.filter(category=category_id, status='y').order_by('importance')
        items_names = [item.name for item in items]
        items_ids = [item.id for item in items]
        items_photos = [Image.objects.filter(item_id=item_id) for item_id in items_ids]
        items_first_photos = [photos.first().photo.url if photos.count() else settings.DEFAULT_PHOTO_URL
                              for photos in items_photos]
        items_cost = [divmod(item.cost, 1) for item in items]
        items_cost = [{'rubles': int(rubles), 'kopeck': int(kopeck * 100)} for rubles, kopeck in items_cost]
        items_info = [item.short_info for item in items]
        items_article = [item.article for item in items]

        return items_names, items_ids, items_article, items_cost, items_info, items_first_photos

    @staticmethod
    def get_categories_data_from_db(subcategories):
        categories_positions = [category.position - 1 for category in subcategories]
        categories_ids = [category.id for category in subcategories]
        categories_names = [category.name for category in subcategories]
        categories_photos = [category.photo.url for category in subcategories]

        return categories_positions, categories_ids, categories_names, categories_photos

    @staticmethod
    def get(request, category_id):
        category = Category.objects.get(id=category_id)
        subcategories = Category.objects.filter(parent_category_id=category_id).order_by('position')

        if subcategories:
            subcategories = CategoryView.get_categories_data_from_db(subcategories)
            categories_positions, categories_ids, categories_names, categories_photos = subcategories

            rows = PackInRows.pack_in_rows_by_position(chain([3], cycle([4, 5])),
                                                       categories_positions,
                                                       ['name', categories_names],
                                                       ['id', categories_ids],
                                                       ['photo', categories_photos])

            context = {'rows': rows}
            template = 'catalogue_categories.html'

        else:
            items = CategoryView.get_items_data_from_db(category_id)
            items_names, items_ids, items_article, items_cost, items_info, items_first_photos = items

            rows = PackInRows.pack_in_rows_by_order(chain([3], cycle([4, 5])),
                                                    ['name', items_names],
                                                    ['id', items_ids],
                                                    ['article', items_article],
                                                    ['cost', items_cost],
                                                    ['info', items_info],
                                                    ['photo', items_first_photos])

            context = {'rows': rows}
            template = 'catalogue_items.html'

        CategoryView.add_navigation(context, category.id, category.name)
        add_categories_to_context(context)
        return render(request, template, context)


class ItemView(View):
    @staticmethod
    def add_navigation(context, item_id, item_name, category_id, category_name):
        CategoryView.add_navigation(context, category_id, category_name)
        context['navigation'] += [{'name': item_name, 'url': reverse('item', args=[item_id, ])}]

    @staticmethod
    def get_data_from_db(item_id):
        item = Item.objects.get(id=item_id)
        photos_urls = [image_object.photo.url for image_object in Image.objects.filter(item_id=item_id)]
        photos_urls = photos_urls if photos_urls else [settings.DEFAULT_PHOTO_URL]
        properties = Property.objects.filter(item_id=item_id).order_by('order')
        rubles, kopeck = divmod(item.cost, 1)

        return item.name, int(rubles), int(kopeck*100), item.article, properties, photos_urls, item.category

    @staticmethod
    def get(request, item_id):
        name, rubles, kopeck, article, properties, photos_urls, category = ItemView.get_data_from_db(item_id)

        context = {'item_name': name,
                   'item_cost_rubles': rubles,
                   'item_cost_kopeck': kopeck,
                   'item_article': article,
                   'photos_urls': photos_urls,
                   'properties': properties}

        add_categories_to_context(context)

        ItemView.add_navigation(context, item_id, name, category.id, category.name)
        return render(request, 'item.html', context)


class SearchView(View):
    @staticmethod
    def add_navigation(context, question):
        IndexView.add_navigation(context)
        context['navigation'] += [{'name': 'Поиск по запросу "' + question + '"', 'url': reverse('search')}]

    @staticmethod
    def get_data_from_db(question):
        items = Item.objects.filter(name__icontains=question, status='y').order_by('importance')
        items_names = [item.name for item in items]
        items_ids = [item.id for item in items]
        items_photos = [Image.objects.filter(item_id=item_id) for item_id in items_ids]
        items_first_photos = [photos.first().photo.url if photos.count() else settings.DEFAULT_PHOTO_URL
                              for photos in items_photos]
        items_cost = [divmod(item.cost, 1) for item in items]
        items_cost = [{'rubles': int(rubles), 'kopeck': int(kopeck * 100)} for rubles, kopeck in items_cost]
        items_info = [item.short_info for item in items]
        items_article = [item.article for item in items]

        return items_names, items_ids, items_article, items_cost, items_info, items_first_photos

    @staticmethod
    def get(request):
        question = request.GET.get("question", "")

        items = SearchView.get_data_from_db(question)
        items_names, items_ids, items_article, items_cost, items_info, items_first_photos = items

        rows = PackInRows.pack_in_rows_by_order(chain([3], cycle([4, 5])),
                                                ['name', items_names],
                                                ['id', items_ids],
                                                ['article', items_article],
                                                ['cost', items_cost],
                                                ['info', items_info],
                                                ['photo', items_first_photos])

        context = {'rows': rows}
        SearchView.add_navigation(context, question)
        add_categories_to_context(context)

        return render(request, 'catalogue_search.html', context)


class ContactsView(View):
    @staticmethod
    def add_navigation(context):
        IndexView.add_navigation(context)
        context['navigation'] += [{'name': 'Контакты', 'url': reverse('contacts')}]

    @staticmethod
    def get_data_from_db(question):
        pass

    @staticmethod
    def get(request):
        context = {}
        ContactsView.add_navigation(context)
        add_categories_to_context(context)
        return render(request, 'contacts.html', context)


class AskQuestionView(View):
    @staticmethod
    def get(request):
        subject = "Вопрос пользователя garmantino.by"
        name = request.GET.get("name", "")
        question = request.GET.get("question", "")
        email = request.GET.get("email", "")
        phone = request.GET.get("phone", "")

        if question and (email or phone):
            message = "Email пользователя: " + email + '\n'
            message += "Имя пользователя: " + name + '\n'
            message += "Телефон пользователя: " + phone + '\n'
            message += "Вопрос пользователя: " + question + '\n'

            try:
                send_mail(subject, message, "garmantinoshop@gmail.com", ['garmantinoshop@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
