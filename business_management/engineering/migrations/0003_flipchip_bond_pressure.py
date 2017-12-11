# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-09 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineering', '0002_flipchip'),
    ]

    operations = [
        migrations.AddField(
            model_name='flipchip',
            name='bond_pressure',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=20),
        ),
    ]
