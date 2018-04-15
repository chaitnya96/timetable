# generic

from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from sheduler.models import *
from .serializers import *


class AllSubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (AllowAny,)


class AllFacultyList(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (AllowAny,)


class AllSemesterList(generics.ListCreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = (AllowAny,)


class AllLectureList(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (AllowAny,)


class AllTimetableList(generics.ListCreateAPIView):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = (AllowAny,)


class SemesterView(generics.RetrieveUpdateDestroyAPIView):  # DetailView CreateView FormView
    lookup_field = 'pk'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = SemesterSerializer

    def get_queryset(self):
        return Semester.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    @permission_classes((AllowAny,))
    def get_all_sem(self, request, *args, **kwargs):
        semesters = Semester.objects.all()
        serialized_semesters = SemesterSerializer(self, semesters, many=True)
        return Response(serialized_semesters.data, status=status.HTTP_200_OK)


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


