# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-11 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0024_auto_20180711_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='type_contractor',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='type_customer',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='type_investor',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='type_other',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='type_potential_customer',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='type_potential_investor',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='type_vendor',
        ),
    ]
