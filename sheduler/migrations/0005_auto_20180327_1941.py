# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-27 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0004_faculty_faculty_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='faculty_type',
        ),
        migrations.AddField(
            model_name='faculty',
            name='lecture_limit',
            field=models.IntegerField(default=18),
        ),
    ]
