# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-02 19:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('address1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('address2', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('zipcode', models.CharField(blank=True, default='', max_length=18, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('email', models.EmailField(max_length=60)),
                ('contact_type', models.CharField(choices=[('VE', 'Vendor'), ('CO', 'Contractor'), ('PC', 'Potential Customer'), ('PI', 'Potential Investor'), ('CU', 'Customer'), ('IN', 'Investor'), ('PA', 'Partner'), ('OT', 'Other')], max_length=2)),
                ('comments', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='FixedAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_tag', models.CharField(max_length=20, unique=True)),
                ('serial_number', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('manufacturer', models.CharField(default='', max_length=100, null=True)),
                ('model_number', models.CharField(default='', max_length=100, null=True)),
                ('description', models.CharField(default='', max_length=100, null=True)),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True)),
                ('purchased_from', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('purchase_condition', models.CharField(choices=[('NE', 'New'), ('US', 'Used'), ('MR', 'Manufacturer Refurbished'), ('RE', 'Refurbished')], default='NE', max_length=2)),
                ('active', models.BooleanField(default=True)),
                ('inactive_date', models.DateField(blank=True, null=True)),
                ('asset_type', models.CharField(choices=[('CE', 'Computer Equipment'), ('OE', 'Office Equipment'), ('LE', 'Lab Equipment'), ('FU', 'Furniture'), ('SO', 'Software')], default='CE', max_length=2)),
                ('location', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('owner', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('comments', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['purchase_date'],
            },
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timesheet_ui', models.CharField(max_length=60, unique=True)),
                ('week_start', models.DateField()),
                ('total_hours', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True)),
                ('employee_signature', models.BooleanField(default=False, null=True)),
                ('employee_sign_date', models.DateField(blank=True, null=True)),
                ('supervisor_signature', models.BooleanField(default=False, null=True)),
                ('supervisor_sign_date', models.DateField(null=True)),
                ('supervisor_comments', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['week_start'],
            },
        ),
        migrations.CreateModel(
            name='TimesheetRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('day_of_week', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], default='MO', max_length=2)),
                ('hours', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True)),
                ('comments', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('timesheet_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Timesheet')),
            ],
            options={
                'ordering': ['row_num'],
            },
        ),
    ]
