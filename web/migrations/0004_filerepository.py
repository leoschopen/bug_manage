# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2022-02-03 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20220202_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.SmallIntegerField(choices=[(1, '文件'), (2, '文件夹')], verbose_name='类型')),
                ('name', models.CharField(help_text='文件/文件夹名', max_length=32, verbose_name='文件夹名称')),
                ('key', models.CharField(blank=True, max_length=128, null=True, verbose_name='文件储存在COS中的KEY')),
                ('file_size', models.IntegerField(blank=True, null=True, verbose_name='文件大小')),
                ('file_path', models.CharField(blank=True, max_length=255, null=True, verbose_name='文件路径')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='web.FileRepository', verbose_name='父级目录')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='最近更新者')),
            ],
        ),
    ]
