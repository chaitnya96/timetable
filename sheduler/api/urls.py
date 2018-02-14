from django.conf.urls import url


from .views import SemesterView, FacultyView, SubjectView, TimetableView

urlpatterns = [
    url(r'^semester/(?P<pk>\d+)/$', SemesterView.as_view(), name='semester'),
    url(r'^faculty/(?P<pk>\d+)/$', FacultyView.as_view(), name='faculty'),
    url(r'^subject/(?P<pk>\d+)/$', SubjectView.as_view(), name='subject'),
    url(r'^timetable/(?P<pk>\d+)/$', TimetableView.as_view(), name='timetable'),

]   