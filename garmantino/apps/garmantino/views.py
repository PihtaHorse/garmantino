# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Category, Item, Image, Property, ItemOnHomePage
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.paginator import Paginator
from django.conf import settings
from django.views.generic import View
from .services.pack_in_rows import PackInRows
from .services.services import add_categories_to_context
from itertools import chain, cycle


class IndexView(View):
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
    def get_data_from_db():
        super_category = Category.objects.get(parent_category_id__isnull=True)
        categories = Category.objects.filter(parent_category_id=super_category.id).order_by('position')
        categories_positions = [category.position for category in categories]
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
        add_categories_to_context(context)
        return render(request, 'catalogue_categories.html', context)


class CategoryView(View):
    @staticmethod
    def get_data_from_db(category_id):
        items = Item.objects.filter(category=category_id, status='y').order_by('importance')
        items_names = [item.name for item in items]
        items_ids = [item.id for item in items]
        items_photos = [Image.objects.filter(item_id=item_id) for item_id in items_ids]
        items_first_photo = [photos.first().photo.url if photos.count() else settings.DEFAULT_PHOTO_URL
                             for photos in items_photos]

        return items_names, items_ids, items_first_photo

    @staticmethod
    def get(request, category_id):
        items_names, items_ids, items_first_photo = CategoryView.get_data_from_db(category_id)

        rows = PackInRows.pack_in_rows_by_order(chain([3], cycle([4, 5])),
                                                ['name', items_names],
                                                ['id', items_ids],
                                                ['photo', items_first_photo])

        context = {'rows': rows}
        add_categories_to_context(context)
        return render(request, 'catalogue_items.html', context)


class ItemView(View):
    @staticmethod
    def get_data_from_db(item_id):
        item = Item.objects.get(id=item_id)
        photos_urls = [image_object.photo.url for image_object in Image.objects.filter(item_id=item_id)]
        photos_urls = photos_urls if photos_urls else [settings.DEFAULT_PHOTO_URL]
        properties = Property.objects.filter(item_id=item_id)

        return item.name, properties, photos_urls

    @staticmethod
    def get(request, item_id):
        item_name, properties, photos_urls = ItemView.get_data_from_db(item_id)

        context = {'item_name': item_name, 'photos_urls': photos_urls, 'properties': properties}
        add_categories_to_context(context)
        return render(request, 'item.html', context)


class SearchView(View):
    @staticmethod
    def get_data_from_db(question):
        items = Item.objects.filter(name__icontains=question, status='y')
        items_ids = [item.id for item in items]
        items_names = [item.name for item in items]
        items_photos = [Image.objects.filter(item_id=item.id) for item in items]
        items_first_photos = [photos.first().photo.url if photos.count() else settings.DEFAULT_PHOTO_URL
                              for photos in items_photos]

        return items_ids, items_names, items_first_photos

    @staticmethod
    def get(request):
        question = request.GET.get("question", "")

        items_ids, items_names, items_first_photo = SearchView.get_data_from_db(question)
        rows = PackInRows.pack_in_rows_by_order(chain([3], cycle([4, 5])),
                                                ['name', items_names],
                                                ['id', items_ids],
                                                ['photo', items_first_photo])

        context = {'rows': rows}
        add_categories_to_context(context)

        return render(request, 'catalogue_search.html', context)
