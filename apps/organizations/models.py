from datetime import datetime

from django.db import models


# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name='城市')
    desc = models.CharField(max_length=300, verbose_name='描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Organizations(models.Model):
    city = models.ForeignKey(CityDict, verbose_name='所属城市')
    category = models.CharField(max_length=20, choices=(('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')), default=
    'pxjg', verbose_name='机构类型')
    name = models.CharField(max_length=50, verbose_name='名称')
    tag = models.CharField(default='全国知名', max_length=20, verbose_name='标签')
    desc = models.CharField(max_length=300, verbose_name='机构描述')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    address = models.CharField(max_length=100, verbose_name='地址')
    image = models.ImageField(upload_to='organizations/%Y/%m', max_length=100, verbose_name='logo')
    course_nums = models.IntegerField(default=0, verbose_name='课程数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_teacher_nums(self):
        return self.teacher_set.all().count()


class Teacher(models.Model):
    organizations = models.ForeignKey(Organizations, verbose_name='所属机构', null=True, blank=True)
    name = models.CharField(max_length=30, verbose_name='名字')
    work_year = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=20, verbose_name='工作公司')
    work_pos = models.CharField(max_length=20, verbose_name='职位')
    point = models.CharField(max_length=100, verbose_name='教学特点')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to='teacher/%Y/%m', max_length=100, verbose_name='头像', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '老师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
