# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-11 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_video_learn_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='path',
            field=models.CharField(default='', max_length=100, verbose_name='视频路径'),
        ),
    ]
