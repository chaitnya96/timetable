# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-20 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0003_auto_20180109_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='Lectures',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='Type',
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_type',
            field=models.CharField(default=b' ', max_length=100),
        ),
    ]
