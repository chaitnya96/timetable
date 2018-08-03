# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-28 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0011_faculty_lecture_limit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='lecture_limit',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]