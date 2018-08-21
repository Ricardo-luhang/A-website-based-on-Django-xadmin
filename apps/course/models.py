from datetime import datetime

from django.db import models

from apps.organizations.models import Organizations, Teacher


# Create your models here.


class Course(models.Model):
    org = models.ForeignKey(Organizations, verbose_name='课程机构', default='', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name='所教教师', default='')
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='描述')
    detail = models.TextField(verbose_name='详情')
    degree = models.CharField(choices=(('gj', '高级'), ('zj', '中级'), ('cj', '初级')), verbose_name='难度等级', max_length=10)
    learn_times = models.IntegerField(default=0, verbose_name='学习时长')
    student = models.IntegerField(default=0, verbose_name='学生数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    image = models.ImageField(upload_to='courses/%Y/%m', max_length=100, verbose_name='封面图', null=True, blank=True)
    is_banner = models.BooleanField(default=False, verbose_name='是否轮播图')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_zj_nums(self):
        return self.section_set.all().count()

    def get_zj(self):
       return self.section_set.all()


class Section(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def get_video(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    section = models.ForeignKey(Section, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长')
    videos = models.FileField(upload_to='videos/%Y/%m', verbose_name='视频', default='', null=True, blank=True)
    path = models.CharField(max_length=100, verbose_name='视频路径', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='资源名')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='下载地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
