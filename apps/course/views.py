from django.shortcuts import render
from utils.mixin_utils import LoginRequireMixin
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from apps.course.models import Course,Section,Video
from apps.operations.models import CourseComment,UserCourse


# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_course = Course.objects.all().order_by('-add_time')
        sort = request.GET.get('sort', '')
        if sort == 'student':
            all_course = all_course.order_by('-student')
        elif sort == 'hot':
            all_course = all_course.order_by('-click_num')

        hot_courses = Course.objects.all().order_by('-click_num')[:3]

        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_course = all_course.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|
                                           Q(detail__icontains=search_keywords))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 3, request=request)
        all_course = p.page(page)
        return render(request, 'course-list.html',
                      {
                          'all_course': all_course,
                          'sort': sort,
                          'hot_courses': hot_courses,
                      })


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        if request.user.is_authenticated():
            user_course = UserCourse.objects.filter(user=request.user, course=course)
            if not user_course:
                user_course = UserCourse(user=request.user, course=course)
                user_course.save()

        course.click_num += 1
        course.save()
        return render(request, 'course-detail.html', {'course': course})


class CourseSectionView(LoginRequireMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.student += 1
        course.save()
        return render(request, 'course-video.html', {'course': course})


class CommentsView(LoginRequireMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_comments = CourseComment.objects.all()
        return render(request, 'course-comment.html',
                      {
                          'course': course,
                          'all_comments': all_comments,
                      }
                      )


class AddComentsView(LoginRequireMixin, View):
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type='application/json')

        course_id = request.POST.get('course_id', 0)
        comments = request.POST.get('comments', '')
        if int(course_id)> 0 and comments:
            course_comments = CourseComment()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')
        else:
            print(comments)
            return HttpResponse('{"status": "fail", "msg": "添加失败"}', content_type='application/json')


class VideoPlayView(LoginRequireMixin, View):
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.section.course
        return render(request, 'course-play.html', {'course': course, 'video': video})


