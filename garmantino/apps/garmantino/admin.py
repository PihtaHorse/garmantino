# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import Item, Property, Image, Category, ItemOnHomePage


class PropertyInline(admin.TabularInline):
    model = Property
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    inlines = (PropertyInline, ImageInline)
    list_display = ('article', 'name', 'status', 'importance', 'pub_date', 'cost')
    list_filter = ('status', 'category')
    search_fields = ('name',)
    date_hierarchy = 'pub_date'
    save_as = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_parent_category_name', 'position', 'pub_date')

    def get_parent_category_name(self, obj):
        if obj.parent_category:
            return obj.parent_category.name
        else:
            return 'Главная категория'

    get_parent_category_name.short_description = 'Родительская категория'


class ItemOnHomePageAdmin(admin.ModelAdmin):
    list_display = ('item', 'position', 'pub_date')

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ItemOnHomePage, ItemOnHomePageAdmin)
