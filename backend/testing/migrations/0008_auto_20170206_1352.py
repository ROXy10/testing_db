# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 13:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0007_test_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='test',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.Question', verbose_name='Питання'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_title',
            field=models.CharField(max_length=512, verbose_name='Відповідь'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False, verbose_name='Правильність'),
        ),
        migrations.AlterField(
            model_name='question',
            name='multi',
            field=models.BooleanField(default=False, verbose_name='Кілька відповідей'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.CharField(max_length=512, verbose_name='Питання'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.Test', verbose_name='Тема теставання'),
        ),
        migrations.AlterField(
            model_name='test',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активний'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_title',
            field=models.CharField(max_length=512, verbose_name='Тема тесту'),
        ),
        migrations.AlterField(
            model_name='testing',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='testing',
            name='result',
            field=models.BooleanField(default=False, verbose_name='Результат'),
        ),
        migrations.AlterField(
            model_name='testing',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.Test', verbose_name='Тема тесту'),
        ),
        migrations.AlterField(
            model_name='testing',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач'),
        ),
    ]
