# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-20 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('testapp', '0003_auto_20160619_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='path',
            field=models.CharField(max_length=10000),
        ),
    ]
