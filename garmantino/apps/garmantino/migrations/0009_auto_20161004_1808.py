# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-04 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0008_auto_20161004_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='category',
            new_name='categories',
        ),
    ]
