# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-25 16:55
from __future__ import unicode_literals

import business_management.financial.models.purchase_orders
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0002_auto_20180725_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.IntegerField(default=business_management.financial.models.purchase_orders.get_po_number, unique=True),
        ),
    ]