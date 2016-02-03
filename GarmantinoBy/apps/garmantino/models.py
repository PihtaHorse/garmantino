# -*- coding: utf-8 -*-
from django.db import models
import os
from django.core.exceptions import ValidationError

def generate_item_image_filename(self, filename):
    url = os.path.join('imgs', 'items', str(self.item.id), filename)
    return url

def generate_category_image_filename(self, filename):
    url = os.path.join('imgs', 'categories', filename)
    return url

ITEM_STATUS_CHOICES = (
    ('m', 'В Производстве'),
    ('y', 'Есть В Наличии'),
    ('n', 'Нет В Наличии'),
    ('o', 'Снят С Производства'),
    ('t', 'Шаблон'),
)

CATEGORY_STATUS_CHOICES = (
    ('n', 'Не Используется'),
    ('y', 'Используется'),
    ('o', 'Устарела'),
)

IMPORTANCE_STATUS_CHOICES = (
    ('a', 'Очень Важный'),
    ('b', 'Важный'),
    ('c', 'Не Важный'),
)

class Category(models.Model):
    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['status']

    name = models.CharField(max_length=100, verbose_name='Название')
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=1, choices=CATEGORY_STATUS_CHOICES, default='n', verbose_name='Статус')
    photo = models.ImageField(upload_to=generate_category_image_filename,
                              default=os.path.join('imgs', 'categories', 'default-category.jpg'),
                              verbose_name='Фотография')
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name='Родительская категория')
    position = models.PositiveSmallIntegerField(null=True,
                                                blank=True,
                                                help_text='Это то, в каком шестиугольнике будет находиться фото. Оставьте пустым, чтобы значение заполнилось автоматически',
                                                verbose_name='Позиция')

    def clean(self):
        if self.parent_category is None:
            if Category.objects.filter(parent_category_id__isnull=True).exclude(id=self.id).count() > 0:
                raise ValidationError('Уже есть вершина иерархии.' + 'Установите родительскую категорию для данной.')
            self.position = 1
        else:
            categories = Category.objects.filter(parent_category_id=self.parent_category.id).exclude(id=self.id).order_by('position')
            categories_positions = [category.position for category in categories]

            if self.position is None or self.position <= 0 or self.position > 35:
                if len(categories_positions) != 0:
                    self.position = categories_positions[-1]+1
                else:
                    self.position = 1
            elif self.position in categories_positions:
                raise ValidationError('Такая позиция уже занята. Заняты:' + str(categories_positions))

    def __str__(self):
        # status = [value for (name, value) in CATEGORY_STATUS_CHOICES if name == self.status]
        name = self.name + ' (' + 'позиция :' + str(self.position) + ')' # + ' (' + status[0] + ')'

        parent_category = self.parent_category
        if parent_category is not None:
            name = parent_category.name + ' --> ' + name

        return name

class Item(models.Model):
    class Meta():
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        ordering = ['pub_date']

    name = models.CharField(max_length=100, verbose_name='Название предмета')
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=1,
                              choices=ITEM_STATUS_CHOICES,
                              default='m',
                              verbose_name='Статус производства')
    category = models.ManyToManyField(Category,
                                      help_text='Выбирать мышкой и кнопкой ctrl. Столик может относиться к нескольким категориям!',
                                      verbose_name='Категория')
    importance = models.CharField(max_length=1,
                              choices=IMPORTANCE_STATUS_CHOICES,
                              default='c',
                              verbose_name='Приоритетность')

    def __str__(self):
        status = [value for (name, value) in ITEM_STATUS_CHOICES if name == self.status]
        return self.name + ' (' + status[0] + ')'

class Property(models.Model):
    class Meta():
        verbose_name = "Свойство"
        verbose_name_plural = "Свойства"

    name = models.CharField(max_length=30, verbose_name='Имя свойства', help_text='Например - цвет')
    value = models.CharField(max_length=100,
                             blank=True,
                             verbose_name='Значение свойства',
                             help_text='Например - красный')
    order = models.IntegerField(default=0,
                                verbose_name='Порядковый номер',
                                help_text='В соответствии с этим номером сортируются свойства. Свойства с маленьким порядковым номером - сверху, с большим - снизу')
    item = models.ForeignKey(Item)

    def __str__(self):
        return self.name + ": " + self.value

class Image(models.Model):
    class Meta():
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"

    photo = models.ImageField(upload_to = generate_item_image_filename,
                              default=os.path.join('imgs', 'items', 'default-item.jpg'),
                              verbose_name='Фото')

    item = models.ForeignKey(Item)




