# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-28 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0009_auto_20180328_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='lecture_limit',
        ),
    ]
