# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-09-11 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0008_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='testcases',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
