# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-22 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0030_faculty_lecture_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]