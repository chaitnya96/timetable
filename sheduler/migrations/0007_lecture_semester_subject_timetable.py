# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-28 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0006_auto_20180124_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_no', models.IntegerField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem_no', models.IntegerField()),
                ('division', models.CharField(max_length=1)),
                ('class_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=50)),
                ('subject_name', models.CharField(max_length=250)),
                ('credits', models.IntegerField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Faculty')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[(b'Monday', b'Monday'), (b'Tuesday', b'Tuesday'), (b'Wednesday', b'Wednesday'), (b'Thursday', b'Thursday'), (b'Friday', b'Friday'), (b'Saturday', b'Saturday')], max_length=10)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Lecture')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Semester')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Subject')),
            ],
        ),
    ]
