from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import requests
#import reversion

class Timesheet(models.Model):
    timesheet_ui = models.CharField(max_length=60, unique=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    week_start = models.DateField(auto_now_add=False)
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    total_hours = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, blank=True, null=True)
    employee_signature = models.BooleanField(default=False, blank=True, null=True)
    employee_sign_date = models.DateField(auto_now_add=False, blank=True, null=True)
    supervisor_signature = models.BooleanField(default=False, blank=True, null=True)
    supervisor_sign_date = models.DateField(auto_now_add=False, null=True)
    supervisor_comments = models.CharField(max_length=255, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['week_start', ]

    def __str__(self):
        return self.timesheet_ui

    def get_absolute_url(self):
        return reverse("administration:timesheet_detail", kwargs={"pk": self.pk})

class TimesheetRow(models.Model):
    #row_num = models.AutoField()
    timesheet_fk = models.ForeignKey(Timesheet)
    description = models.CharField(max_length=255, default='', blank=True, null=True)

    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY ='WE'
    THURSDAY ='TH'
    FRIDAY ='FR'
    SATURDAY ='SA'
    SUNDAY ='SU'

    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )
    day_of_week = models.CharField(
        max_length=2,
        choices=DAY_CHOICES,
        default=MONDAY,
    )

    hours = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, blank=True, null=True)
    comments = models.CharField(max_length=255, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['row_num', ]

    def __str__(self):
        return self.row_num

    def get_absolute_url(self):
        return reverse("administration:row_num_detail", kwargs={"pk": self.pk})
