# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-17 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_organizations_course_nums'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizations',
            name='tag',
            field=models.CharField(default='全国知名', max_length=20, verbose_name='标签'),
        ),
    ]
