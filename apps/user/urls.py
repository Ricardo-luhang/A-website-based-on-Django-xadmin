from django.conf.urls import url, include

from apps.user.views import UserInfoView,UploadIamgView,MyCourseView

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    url(r'^image_load/$', UploadIamgView.as_view(), name='image_load'),
    url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse')
]