# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 00:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_auto_20170205_0025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Тема тестування', 'verbose_name_plural': 'Теми тестування'},
        ),
        migrations.AlterModelOptions(
            name='testing',
            options={'verbose_name': 'Результати теста', 'verbose_name_plural': 'Результати тестів'},
        ),
    ]
