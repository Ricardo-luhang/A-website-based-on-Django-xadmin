from datetime import datetime

from django.db import models

from apps.course.models import Course
from apps.user.models import UserInfo


# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    course_name = models.CharField(max_length=50, verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户询问'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseComment(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
    comments = models.CharField(max_length=300, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='用户')
    message = models.CharField(max_length=300, verbose_name='消息')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='用户')
    fav_id = models.IntegerField(default=0, verbose_name='数据ID')
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '机构'), (3, '教师')), default=1)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

