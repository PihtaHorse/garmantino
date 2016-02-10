# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.garmantino.models import Category, Item, Image, Property, ItemOnHomePage
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

CELLS_NUMBER = [0, 3, 7, 10, 14, 17, 21, 24, 28, 31, 35]
               #0  3  4   3   4   3   4   3   4   3   4   Колличество свбодных клеток в ряду
CELLS_NUMBER_V2 = [0, 5, 9, 14, 19, 24, 29, 34, 39, 44, 49]
                  #0  5  4   5   4   5   4   5   4   5   4   Колличество свбодных клеток в ряду

def index(request):
    items = [obj.item for obj in ItemOnHomePage.objects.order_by('importance')]
    photos = [item.image_set.first().photo for item in items]
    photos_urls = [photo.url for photo in photos]
    items_ids = [item.id for item in items]
    img_ids = ['pic1', 'pic2', 'pic3', 'pic4']

    context = {'photos_urls': photos_urls, 'items_ids': items_ids, 'img_ids': img_ids}
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
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print(items_number)
                print(i)
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                if i <= items_number:
                    items[i-1].photo = Image.objects.filter(item_id=items[i-1].id).first()
                    cells.append(items[i-1])
                else:
                    cells.append(None)
            rows.append(cells)

        print(rows_number)
        for row in range(0, rows_number):
            for cell in rows[row]:
                print(str(cell))
            print('***********************************************')
        print(rows)

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

    for position in categories_positions:
        print( position )


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
