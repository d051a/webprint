# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-09 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0033_auto_20191209_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recepient',
            name='adds',
        ),
    ]
