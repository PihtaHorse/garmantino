# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pub_date'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]