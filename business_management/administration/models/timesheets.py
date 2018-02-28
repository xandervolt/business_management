from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import requests
#import reversion

class Timesheet(models.Model):
    timesheet_ui = models.CharField(max_length=60, unique=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    week_start = models.DateField(auto_now_add=False)
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL)
    total_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, blank=True, null=True)
    employee_signature = models.BooleanField(default=False)
    employee_sign_date = models.DateField(auto_now_add=False)
    supervisor_signature = models.BooleanField(default=False)
    supervisor_sign_date = models.DateField(auto_now_add=False)
    supervisor_comments = models.CharField(max_length=255, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['week_start', ]

    def __str__(self):
        return self.timesheet_ui

    def get_absolute_url(self):
        return reverse("administration:timesheet_detail", kwargs={"pk": self.pk})

class TimesheetRow(models.Model):
    row_num = models.AutoField()
    timesheet_fk = models.ForeignKey(models.Timesheet)
    monday_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, blank=True, null=True)
    tuesday_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, blank=True, null=True)
    wednesday_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, blank=True, null=True)
    thursday_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, blank=True, null=True)
    friday_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, blank=True, null=True)
    saturday_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, blank=True, null=True)
    sunday_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, blank=True, null=True)
    comments = models.CharField(max_length=255, default='', blank=True, null=True)

    class Meta:
        ordering = ['row_num', ]

    def __str__(self):
        return self.row_num

    def get_absolute_url(self):
        return reverse("administration:row_num_detail", kwargs={"pk": self.pk})