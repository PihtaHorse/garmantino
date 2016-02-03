# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.garmantino.models import Category, Item, Image, Property
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

CELLS_NUMBER = [0, 3, 7, 10, 14, 17, 21, 24, 28, 31, 35]
               #3  4   3   4   3   4   3   4   3   4 Колличество свбодных клеток в ряду

def index(request):
    context ={}
    return render(request, 'index.html', context)

def category(request, category_id):
    items = Item.objects.filter(category=category_id).exclude(status='t').order_by('importance')
    items_number = len(items)
    rows_number = 0
    rows = []

    if len(items) != 0:
        while CELLS_NUMBER[rows_number] < items_number:
            rows_number += 1

        for row in range(0, rows_number):
            cells = []
            for i in range(CELLS_NUMBER[row]+1, CELLS_NUMBER[row+1]+1):
                if i < items_number:
                    items[i].photo = Image.objects.filter(item_id=items[i].id).first()
                    cells.append(items[i])
                else:
                    cells.append(None)
            rows.append(cells)

        print(rows_number)
        for row in range(0, rows_number):
            for cell in rows[row]:
                print(str(cell))
            print('***********************************************')

    context = {'rows':rows, 'is_rows_number_odd': len(rows)%2 == 1}
    return render(request, 'category.html', context)

def catalogue(request):
    try:
        super_category = Category.objects.get(parent_category_id__isnull=True)
    except ObjectDoesNotExist:
        print("**************There is no any super-categories yet.**************")
    except MultipleObjectsReturned:
        print("**************There is more than one super-categories.**************")

    categories = Category.objects.filter(parent_category_id=super_category.id).order_by('position')
    categories_positions = [category.position for category in categories]
    rows = []

    if len(categories) != 0:
        rows_number = 0
        counter = 0

        while CELLS_NUMBER[rows_number] < max(categories_positions):
            rows_number += 1

        for row in range(0, rows_number):
            cells = []
            for i in range(CELLS_NUMBER[row]+1, CELLS_NUMBER[row+1]+1):
                if i in categories_positions:
                    cells.append(categories[counter])
                    counter += 1
                else:
                    cells.append(None)
            rows.append(cells)

        # for row in range(0, rows_number):
        #     for cell in rows[row]:
        #         print(str(cell))
        #     print('***********************************************')

    context = {'rows':rows, 'is_rows_number_odd': len(rows)%2 == 1}
    return render(request, 'catalogue.html', context)

def item(request, item_id):
    item = Item.objects.get(id=item_id)
    photos_urls = [image_object.photo.url for image_object in Image.objects.filter(item_id=item_id)]
    properties = Property.objects.filter(item_id=item_id)

    print(photos_urls)

    context = {'item': item, 'photos_urls': photos_urls, 'properties':properties}
    return render(request, 'item.html', context)
