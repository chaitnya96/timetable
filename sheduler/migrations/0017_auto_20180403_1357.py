# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-03 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0016_auto_20180401_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='is_lab',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timetable',
            name='lab_class',
            field=models.CharField(blank=True, choices=[('1A-1B', '1A-1B'), ('1A-1C', '1A-1C'), ('1A-1D', '1A-1D'), ('1B-1C', '1B-1C'), ('1B-1D', '1B-1D'), ('1C-1D', '1C-1D'), ('2A-2B', '2A-2B'), ('2A-2C', '2A-2C'), ('2A-2D', '2A-2D'), ('2B-2C', '2B-2C'), ('2B-2D', '2B-2D'), ('2C-2D', '2C-2D')], max_length=6),
        ),
    ]