# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-30 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineering', '0022_auto_20180430_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gaaswaferdesign',
            name='design_document',
            field=models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
