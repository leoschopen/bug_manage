# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2022-04-27 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20220426_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='任务位置'),
        ),
    ]