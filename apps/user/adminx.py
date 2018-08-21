import xadmin
from xadmin import views

from .models import UserInfo, EmailCaptcha, Viewpager


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '乐之在线后台管理'
    site_footer = '乐之在线学习平台'
    menu_style = 'accordion'


class UserInfoAdmin(object):
    list_display = ['nick_name', 'age', 'birth_day', 'gender', 'address', 'mobile_num', 'image']
    search_fields = ['nick_name', 'age', 'birth_day', 'gender', 'address', 'mobile_num']
    list_filter = ['nick_name', 'age', 'birth_day', 'gender', 'address', 'mobile_num', 'image']


class EamilCaptchaAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class ViewpagerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.unregister(UserInfo)
xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(EmailCaptcha, EamilCaptchaAdmin)
xadmin.site.register(Viewpager, ViewpagerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


