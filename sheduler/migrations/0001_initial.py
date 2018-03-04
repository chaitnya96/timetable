# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-04 08:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('country_code', models.IntegerField(blank=True, null=True)),
                ('contact_no', models.BigIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_password_changed', models.BooleanField(default=False)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Qualification', models.CharField(default='MCA', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_type', models.CharField(max_length=250)),
            ],
        ),
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
                ('semester_number', models.IntegerField()),
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
                ('semester', models.IntegerField()),
                ('credits', models.IntegerField(default=0)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Lecture')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Semester')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='UserResetPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid_key', models.BooleanField(default=False)),
                ('key', models.CharField(blank=True, max_length=40)),
                ('key_expires', models.DateTimeField()),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_reset_password',
            },
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.FacultyType'),
        ),
    ]
