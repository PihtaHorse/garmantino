# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0015_itemonhomepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemonhomepage',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='garmantino.Item', verbose_name='Предмет для главной'),
        ),
    ]
