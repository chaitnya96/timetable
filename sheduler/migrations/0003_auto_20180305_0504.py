# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-05 05:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0002_auto_20180305_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='credits',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_code',
        ),
    ]