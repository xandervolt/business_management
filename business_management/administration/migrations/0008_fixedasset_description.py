# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-28 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_auto_20180227_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedasset',
            name='description',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]