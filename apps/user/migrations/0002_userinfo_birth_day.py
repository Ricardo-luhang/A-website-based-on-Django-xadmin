# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-29 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='birth_day',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
    ]
