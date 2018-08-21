from django.conf.urls import url, include
from apps.organizations.views import OrgListView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView


urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name='orglist'),
    url(r'^home/(?P<org_id>\d+)', OrgHomeView.as_view(), name='org_home'),
    url(r'^course/(?P<org_id>\d+)', OrgCourseView.as_view(), name='org_course'),
    url(r'^desc/(?P<org_id>\d+)', OrgDescView.as_view(), name='org_desc'),
    url(r'^teacher/(?P<org_id>\d+)', OrgTeacherView.as_view(), name='org_teacher'),

]