# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0009_auto_20170910_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Url2',
            field=models.URLField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Url3',
            field=models.URLField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Url4',
            field=models.URLField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Url5',
            field=models.URLField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
