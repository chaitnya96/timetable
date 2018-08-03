# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-01 09:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0015_faculty_lecture_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='lecture_limit',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(18), django.core.validators.MinValueValidator(0)]),
        ),
    ]