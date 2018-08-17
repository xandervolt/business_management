# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-14 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clockpunch',
            name='hours_for_the_day',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=4, null=True),
        ),
    ]