# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20170205_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testing',
            name='date',
            field=models.DateField(),
        ),
    ]
