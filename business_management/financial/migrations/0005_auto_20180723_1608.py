# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-23 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0004_auto_20180723_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='terms',
            field=models.CharField(choices=[('CC', 'Credit Card'), ('15', 'Net 15'), ('30', 'Net 30')], default='CC', max_length=2),
        ),
    ]