from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserInfo(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    age = models.IntegerField(verbose_name='年龄', default=18)
    birth_day = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    address = models.CharField(max_length=100, verbose_name='地址')
    mobile_num = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    image = models.ImageField(upload_to='image/%Y/%m', default='/media/default.png', verbose_name='头像', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailCaptcha(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '忘记密码')), default='register', max_length=10, verbose_name='类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Viewpager(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='viewpager/%Y/%m', max_length=100, verbose_name='图片', null=True, blank=True)
    url = models.CharField(max_length=200, verbose_name='图片链接')
    index = models.IntegerField(default=100, verbose_name='序号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


