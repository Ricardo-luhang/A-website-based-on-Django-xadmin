# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-05 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20180604_0925'),
        ('course', '0002_auto_20180602_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='org',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='organizations.Organizations', verbose_name='课程机构'),
        ),
    ]
