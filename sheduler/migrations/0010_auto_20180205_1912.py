# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-05 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0009_auto_20180205_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='Name',
            new_name='name',
        ),
    ]