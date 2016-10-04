# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0006_auto_20160913_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='article',
            field=models.CharField(max_length=15, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.FloatField(max_length=10, verbose_name='Цена'),
        ),
    ]
