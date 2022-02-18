# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2022-02-18 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20220217_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, unique=True, verbose_name='邀请码')),
                ('count', models.PositiveIntegerField(blank=True, help_text='空表示无数量限制', null=True, verbose_name='限制数量')),
                ('use_count', models.PositiveIntegerField(default=0, verbose_name='已邀请数量')),
                ('period', models.IntegerField(choices=[(30, '30分钟'), (60, '1小时'), (300, '5小时'), (1440, '24小时')], default=1440, verbose_name='有效期')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_invite', to='web.UserInfo', verbose_name='创建者')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目')),
            ],
        ),
    ]
