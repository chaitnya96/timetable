# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-12 05:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0026_auto_20180412_0457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='lecture_limit',
        ),
    ]
