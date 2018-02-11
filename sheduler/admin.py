# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Faculty, Semester, Subject, Lecture, Timetable, FacultyType

# Register your models here.
admin.site.register(Faculty)
admin.site.register(FacultyType)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Lecture)
admin.site.register(Timetable)


