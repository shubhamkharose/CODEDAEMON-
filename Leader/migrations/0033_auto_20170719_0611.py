# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leader', '0032_auto_20170719_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cont_3',
            name='sub_time',
            field=models.DateTimeField(),
        ),
    ]