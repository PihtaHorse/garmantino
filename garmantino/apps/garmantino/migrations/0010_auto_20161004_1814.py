# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-04 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0009_auto_20161004_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_category', to='garmantino.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.ManyToManyField(to='garmantino.Category', verbose_name='Категори'),
        ),
    ]
