# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, ListView
from .models import Timetable, Faculty
from rest_framework.views import APIView



class index(APIView):
    model = Timetable
    template_name = "sheduler/index.html"
    context_object_name = 'subjects'


class faculty(ListView):
    model = Faculty
    template_name = "sheduler/faculty_name.html"
    context_object_name = 'faculty'


class temp(TemplateView):
    template_name = "sheduler/temp.html"
