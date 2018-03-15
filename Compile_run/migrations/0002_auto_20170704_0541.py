# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-04 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compile_run', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.CharField(max_length=20)),
                ('problem_statement', models.CharField(max_length=150)),
                ('problem_sub', models.IntegerField(verbose_name=0)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.IntegerField(verbose_name=0)),
                ('Lang', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=1000)),
                ('time', models.DateTimeField()),
                ('pts', models.IntegerField()),
                ('res', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='session_code',
        ),
        migrations.AddField(
            model_name='user',
            name='cpp_session_code',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='java_session_code',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='py_session_code',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]