from django.conf.urls import url, include

from apps.course.views import CourseListView,CourseDetailView,CourseSectionView,CommentsView,AddComentsView,\
    VideoPlayView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='courselist'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='coursedetail'),
    url(r'^section/(?P<course_id>\d+)/$', CourseSectionView.as_view(), name='course_section'),
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comments'),
    url(r'^add_comment/$', AddComentsView.as_view(), name='add_comment'),
    url(r'^video_play/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name='video_play'),

]