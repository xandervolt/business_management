# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-23 17:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_ui',
        ),
    ]