import xadmin

from .models import CityDict,Organizations,Teacher


class CityAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class OrganizationsAdmin(object):
    list_display = ['city', 'name', 'desc', 'click_num', 'fav_num', 'address', 'image', 'add_time']
    search_fields = ['city', 'name', 'desc', 'click_num', 'fav_num', 'address', 'image']
    list_filter = ['city', 'name', 'desc', 'click_num', 'fav_num', 'address', 'image', 'add_time']


class TeacherAdmin(object):
    list_display = ['organizations', 'name', 'work_year', 'work_company', 'work_pos', 'point', 'click_num', 'fav_num',
                    'add_time']
    search_fields = ['organizations', 'name', 'work_year', 'work_company', 'work_pos', 'point', 'click_num', 'fav_num']
    list_filter = ['organizations', 'name', 'work_year', 'work_company', 'work_pos', 'point', 'click_num', 'fav_num',
                   'add_time']


xadmin.site.register(CityDict, CityAdmin)
xadmin.site.register(Organizations, OrganizationsAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

