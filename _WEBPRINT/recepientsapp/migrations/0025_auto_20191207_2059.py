# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-07 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0024_auto_20191207_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]