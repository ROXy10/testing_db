# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 00:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_auto_20170205_0018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Теми тестування', 'verbose_name_plural': 'Список тем тестування'},
        ),
        migrations.AlterModelOptions(
            name='testing',
            options={'verbose_name': 'Тести', 'verbose_name_plural': 'Список тестів'},
        ),
    ]
