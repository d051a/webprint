# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-09 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0030_auto_20191208_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название реестра')),
                ('template', models.FileField(upload_to='', verbose_name='Шаблон реестра')),
            ],
            options={
                'verbose_name': 'Тип реестра',
                'verbose_name_plural': 'Типы реестра',
                'ordering': ['-pk'],
            },
        ),
        migrations.AlterField(
            model_name='registry',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepientsapp.RegistryType', verbose_name='Тип реестра'),
        ),
    ]
