from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
# Create your views here.
from apps.organizations.models import CityDict, Organizations
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class OrgListView(View):
    def get(self, request):
        all_city = CityDict.objects.all()
        all_orgs = Organizations.objects.all()

        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        all_num = all_orgs.count()

        ranks = all_orgs.order_by('fav_num')

        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 2, request=request)
        all_org = p.page(page)
        return render(request, 'org-list.html',
                      {'all_city': all_city,
                       'all_org': all_org,
                       'all_num': all_num,
                       'city_id': city_id,
                       'category': category,
                       'ranks': ranks,
                       }
                      )


class OrgHomeView(View):
    def get(self, request, org_id):
        current_page = 'home'
        course_org = Organizations.objects.get(id=int(org_id))
        all_course = course_org.course_set.all()[:3]
        all_teacher = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html',
                      {'all_course': all_course,
                       'all_teacher': all_teacher,
                       'course_org': course_org,
                       'current_page': current_page
                       }
                      )


class OrgCourseView(View):
    def get(self, request, org_id):
        current_page = 'course'
        course_org = Organizations.objects.get(id=int(org_id))
        all_course = course_org.course_set.all()
        return render(request, 'org-detail-course.html',
                      {'all_course': all_course,
                       'course_org': course_org,
                       'current_page': current_page
                       }
                      )


class OrgDescView(View):
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = Organizations.objects.get(id=int(org_id))
        return render(request, 'org-detail-desc.html', {'course_org': course_org, 'current_page': current_page})


class OrgTeacherView(View):
    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = Organizations.objects.get(id=int(org_id))
        all_teacher = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {'course_org': course_org, 'all_teacher': all_teacher, 'current_page': current_page})