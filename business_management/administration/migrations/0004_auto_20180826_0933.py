# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-26 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20180826_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='time_delta',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
