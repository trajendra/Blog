# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-14 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20161015_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=-1),
        ),
    ]
