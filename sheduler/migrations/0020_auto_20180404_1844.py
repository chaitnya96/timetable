# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-04 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0019_auto_20180404_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='lab_faculty',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sheduler.Faculty'),
        ),
    ]
