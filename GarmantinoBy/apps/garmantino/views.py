# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Category, Item, Image, Property, ItemOnHomePage
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.paginator import Paginator
from random import shuffle
from django.conf import settings

CELLS_NUMBER = [0, 3, 7, 10, 14, 17, 21, 24, 28, 31, 35]
               # 0  3  4   3   4   3   4   3   4   3   4   Колличество свбодных клеток в ряду

CELLS_NUMBER_V2 = [0, 4, 9, 13, 18, 22, 27, 31, 36]
                 # 0  4  5   4   5   4   5   4   5   Колличество свбодных клеток в ряду


def index(request):
    items = [obj.item for obj in ItemOnHomePage.objects.order_by('position')]
    items_positions = [obj.position for obj in ItemOnHomePage.objects.order_by('position')]
    items_photos = [item.image_set.first() for item in items]
    items_photos_urls = [photo.photo.url if photo else settings.DEFAULT_PHOTO_URL for photo in items_photos]
    items_ids = [item.id for item in items]
    animation_duration = 6.25 * len(items)
    animation_delay = [-6.25 * i for i in range(0, len(items))]
    rows = [[None, None, None, None, None]]  # Добавляем один пустой ряд сверху
    rows_number = 5
    counter = 0

    shuffle(animation_delay)  # Перемешаем, чтобы было веселей и анимаци каждый раз была разной

    for row in range(0, rows_number):
        cells = []
        for i in range(CELLS_NUMBER_V2[row]+1, CELLS_NUMBER_V2[row+1]+1):
            if i in items_positions:
                css_token = 'animation: anim1 ' + str(animation_duration) + 's linear ' + str(animation_delay[counter]) + 's infinite;'
                cells.append({'item_photo_url': items_photos_urls[counter], 'item_id': items_ids[counter], 'css_token': css_token})
                counter += 1
            else:
                cells.append(None)
        if row % 2 == 0:
            cells.insert(0, None)
            cells.append(None)
        rows.append(cells)

    context = {'rows': rows, 'is_rows_number_odd': len(rows) % 2 == 1, 'items_photos_urls': items_photos_urls, 'items_ids': items_ids}
    return render(request, 'index.html', context)


def search(request):
    question = ''
    items = []
    results = []
    page_number = 1

    if request.method == 'GET':
        question = request.GET.get("question", "")
        page_number = request.GET.get("page", "1")
        items = Item.objects.filter(name__icontains=question)

        for item in items:
            photos = Image.objects.filter(item_id=item.id)
            categories = Category.objects.filter(item=item)
            categories = [{'name': category.name, 'id': category.id} for category in categories]
            result = {'id': item.id, 'name': item.name, 'categories': categories}

            print(photos.first(), type(photos.first()))
            if photos.count():
                result['photo'] = photos.first().photo.url
            else:
                result['photo'] = settings.DEFAULT_PHOTO_URL
            results.append(result)

    current_page = Paginator(results, 2)
    context = {'results': current_page.page(page_number), 'question': question}
    return render(request, 'search.html', context)


def category(request, category_id):
    items = Item.objects.filter(category=category_id).exclude(status='t').order_by('importance')
    items_number = len(items)
    rows_number = 0
    rows = []

    if items_number != 0:
        while CELLS_NUMBER[rows_number] < items_number:
            rows_number += 1
        rows_number += 1  # Добавляем 1, чтобы всегда был последний пустой ряд

        for row in range(0, rows_number):
            cells = []
            for i in range(CELLS_NUMBER[row]+1, CELLS_NUMBER[row+1]+1):
                if i <= items_number:
                    photos = Image.objects.filter(item_id=items[i-1].id)
                    if photos.count():
                        items[i-1].photo = photos.first().photo.url
                    else:
                        items[i-1].photo = settings.DEFAULT_PHOTO_URL
                    cells.append(items[i-1])
                else:
                    cells.append(None)
            if row % 2 == 0:
                cells.insert(0, None)
                cells.append(None)
            rows.append(cells)

    context = {'rows': rows, 'is_rows_number_odd': len(rows) % 2 == 1}
    return render(request, 'category.html', context)


def catalogue(request):
    super_category = Category.objects.get(parent_category_id__isnull=True)
    categories = Category.objects.filter(parent_category_id=super_category.id).order_by('position')
    categories_positions = [category.position for category in categories]
    rows = []
    rows_number = 0
    counter = 0

    if len(categories) != 0:
        while CELLS_NUMBER[rows_number] < max(categories_positions):
            rows_number += 1
        rows_number += 1  # Добавляем 1, чтобы всегда был последний пустой ряд

        for row in range(0, rows_number):
            cells = []
            for i in range(CELLS_NUMBER[row]+1, CELLS_NUMBER[row+1]+1):
                if i in categories_positions:
                    cells.append(categories[counter])
                    counter += 1
                else:
                    cells.append(None)
            if row % 2 == 0:
                cells.insert(0, None)
                cells.append(None)
            rows.append(cells)

    context = {'rows': rows, 'is_rows_number_odd': len(rows) % 2 == 1}
    return render(request, 'catalogue.html', context)


def item(request, item_id):
    item = Item.objects.get(id=item_id)
    photos_urls = [image_object.photo.url for image_object in Image.objects.filter(item_id=item_id)]
    properties = Property.objects.filter(item_id=item_id)

    context = {'item': item, 'photos_urls': photos_urls, 'properties': properties}
    return render(request, 'item.html', context)
