from django.conf.urls import url, include
from .views import temp, faculty, index

urlpatterns = [
    url(r'^$', index.as_view()),
    url(r'^Faculty$', faculty.as_view()),
    url(r'^temp/$', temp.as_view()),
    url(r'^api/', include('sheduler.api.urls')),


]
