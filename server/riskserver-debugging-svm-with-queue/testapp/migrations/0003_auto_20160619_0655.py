# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-19 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('testapp', '0002_auto_20160524_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='path',
            field=models.FileField(upload_to=b''),
        ),
    ]