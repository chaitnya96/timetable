# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-04 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0023_remove_timetable_lab_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='lab_faculty',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
