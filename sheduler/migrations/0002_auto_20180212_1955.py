# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-12 19:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='sem_no',
            new_name='semester_number',
        ),
    ]
