from django.contrib import admin

# Register your models here.
from .models import Item
from .models import Property
from .models import Image
from .models import Category

class PropertyInline(admin.TabularInline):
    model = Property
    extra = 1

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    inlines = [
        PropertyInline,
        ImageInline
    ]
    date_hierarchy = 'pub_date'
    save_as = True
    list_filter = ('status', 'category')

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)