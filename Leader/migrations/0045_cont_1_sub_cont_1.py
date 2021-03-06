# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0005_auto_20170724_1513'),
        ('home', '0014_contact'),
        ('Leader', '0044_auto_20170728_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='cont_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_time', models.DateTimeField(blank=True)),
                ('tot_score', models.IntegerField(default=0)),
                ('Magical_String', models.IntegerField(default=0)),
                ('Scan_Me', models.IntegerField(default=0)),
                ('Cousins', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
            options={
                'ordering': ['-tot_score', 'sub_time'],
            },
        ),
        migrations.CreateModel(
            name='Sub_cont_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10000)),
                ('time', models.DateTimeField()),
                ('Lang', models.CharField(max_length=10)),
                ('pts', models.IntegerField(default=0)),
                ('res', models.CharField(max_length=100)),
                ('Problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Problem')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
