# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2022-04-29 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_projectuser_task_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='task_price',
        ),
    ]
