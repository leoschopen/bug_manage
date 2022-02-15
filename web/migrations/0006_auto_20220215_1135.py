# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2022-02-15 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20220209_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=80, verbose_name='主题')),
                ('desc', models.TextField(verbose_name='问题描述')),
                ('priority', models.CharField(choices=[('danger', '高'), ('warning', '中'), ('success', '低')], default='danger', max_length=12, verbose_name='优先级')),
                ('status', models.SmallIntegerField(choices=[(1, '新建'), (2, '处理中'), (3, '已解决'), (4, '已忽略'), (5, '待反馈'), (6, '已关闭'), (7, '重新打开')], default=1, verbose_name='状态')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='开始时间')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结束时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('latest_update_datetime', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('assign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='web.UserInfo', verbose_name='指派')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_problems', to='web.UserInfo', verbose_name='创建者')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='阶段名称')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目')),
            ],
        ),
        migrations.AddField(
            model_name='issues',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Module', verbose_name='阶段'),
        ),
        migrations.AddField(
            model_name='issues',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目'),
        ),
    ]
