# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-09-24 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0106_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='municipality',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Kommune'),
        ),
    ]
