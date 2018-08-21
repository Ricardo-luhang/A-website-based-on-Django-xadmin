"""goodstudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
import xadmin
from django.views.generic import TemplateView
from django.views.static import serve
from goodstudy.settings import MEDIA_ROOT

from user.views import LoginView, RegisterView, ActiveView, ForgetpwdView, ResetpwdView, ModefyPwdView, LogoutView,IndexView
from organizations.views import OrgListView,OrgHomeView
import captcha.urls

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include(captcha.urls)),
    url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name='active'),
    url(r'^forgetpwd/$', ForgetpwdView.as_view(), name='forgetpwd'),
    url(r'^resetpwd/(?P<active_code>.*)/$', ResetpwdView.as_view(), name='active'),
    url(r'^modefypwd/$', ModefyPwdView.as_view(), name='modefy_pwd'),

    url(r'^org/', include('organizations.urls', namespace='org')),
    url(r'^course/', include('course.urls', namespace='course')),
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url(r'^users/', include('user.urls', namespace='user')),



]
