# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0011_auto_20160202_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Оставьте пустым, чтобы значение заполнилось автоматически', null=True),
        ),
    ]