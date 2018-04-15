from django.conf.urls import url


from .views import *

urlpatterns = [
    url(r'^semester/(?P<pk>\d+)/$', SemesterView.as_view(), name='semester'),
    url(r'^faculty/(?P<pk>\d+)/$', FacultyView.as_view(), name='faculty'),
    url(r'^subject/(?P<pk>\d+)/$', SubjectView.as_view(), name='subject'),
    url(r'^timetable/(?P<pk>\d+)/$', TimetableView.as_view(), name='timetable'),
    url(r'allSubject', AllSubjectList.as_view(), name='AllSemester '),
    url(r'allFaculty', AllFacultyList.as_view(), name='AllFaculty '),
    url(r'allSemester', AllSemesterList.as_view(), name='AllFaculty '),
    url(r'allLecture', AllLectureList.as_view(), name='AllFaculty '),
    url(r'allTimetable', AllTimetableList.as_view(), name='AllFaculty '),

    ]