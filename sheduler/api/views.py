# generic

from rest_framework import generics

from sheduler.models import Semester, Faculty, Subject, Timetable
from .serializers import SemesterSerializer, FacultySerializer, SubjectSerializer, TimetableSerializer


class SemesterView(generics.RetrieveUpdateDestroyAPIView):  # DetailView CreateView FormView
    lookup_field = 'pk'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = SemesterSerializer

    def get_queryset(self):
        return Semester.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class FacultyView(generics.RetrieveUpdateDestroyAPIView):  # DetailView CreateView FormView
    lookup_field = 'pk'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = FacultySerializer

    def get_queryset(self):
        return Faculty.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class SubjectView(generics.RetrieveUpdateDestroyAPIView):  # DetailView CreateView FormView
    lookup_field = 'pk'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return Subject.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class TimetableView(generics.RetrieveUpdateDestroyAPIView):  # DetailView CreateView FormView
    lookup_field = 'pk'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = TimetableSerializer

    def get_queryset(self):
        return Timetable.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}



