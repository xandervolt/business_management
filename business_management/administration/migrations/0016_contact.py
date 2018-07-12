# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-10 22:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administration', '0015_auto_20180516_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('company', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('mobile_number', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('fax_number', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('zipcode', models.CharField(blank=True, default='', max_length=18, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('type_vendor', models.BooleanField(default='')),
                ('type_contractor', models.BooleanField(default='')),
                ('type_potential_customer', models.BooleanField(default='')),
                ('type_potential_investor', models.BooleanField(default='')),
                ('type_customer', models.BooleanField(default='')),
                ('type_investor', models.BooleanField(default='')),
                ('type_other', models.BooleanField(default='')),
                ('comments', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
