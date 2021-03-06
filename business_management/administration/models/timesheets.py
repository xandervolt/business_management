from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.core.urlresolvers import reverse
import requests
import datetime
import pytz
from django.utils import timezone
#import reversion

tz=pytz.timezone('America/Denver')

'''
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

'''

USER_ACTIVITY_CHOICES = (
    ('checkin', 'Check In'),
    ('checkout', 'Check Out'),
)

class UserActivityManager(models.Manager):

    def current(self, user):
        current_obj = self.get_queryset().filter(user=user).order_by('-timestamp').first()
        return current_obj

    def last_checkin_time(self, user):
        last_activity_time = self.get_queryset().order_by('-timestamp').filter(user=user, activity="checkin").first()
        return last_activity_time

    def toggle(self, user):
        last_item = self.current(user)
        activity = "checkin"
        time_delta = None
        if last_item is not None:
            if last_item.timestamp <= tz.localize(datetime.datetime.now()):
                pass
            if last_item.activity == "checkin":
                activity = "checkout"
                last_checkin = self.last_checkin_time(user)
                last_checkin_local_time = tz.normalize(last_checkin.timestamp)
                time_delta = tz.localize(datetime.datetime.now()) - last_checkin_local_time

        obj = self.model(
                user=user,
                activity=activity,
                time_delta = time_delta,
        )
        obj.save()
        return obj


class UserActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    activity = models.CharField(max_length=120, default='checkin', choices=USER_ACTIVITY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    time_delta = models.CharField(max_length=25, blank=True, null=True)
    project = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    objects = UserActivityManager()

    def __unicode__(self):
        return str(self.activity)

    def __str__(self):
        return str(self.activity)

    class Meta:
        verbose_name = 'User Activity'
        verbose_name_plural = "User Activities"

    def next_activity(self):
        next = "Check in"
        if self.activity == "checkin":
            next = "Check out"
        return next

    @property
    def current(self):
        current = 'Checked Out'
        if self.activity == 'checkin':
            current = "Checked in"
        return current

    def clean(self, *args, **kwargs):
        if self.user:
            user_activities = UserActivity.objects.exclude(
                                id=self.id
                            ).filter(
                                user = self.user
                            ).order_by('-timestamp')
            if user_activities.exists():
                recent_ = user_activities.first()
                if self.activity == recent_.activity:
                    message = "%s is not a valid activity for this user" %(self.get_activity_display())
                    raise ValidationError(message)
            else:
                if self.activity != "checkin":
                    message = "%s is not a valid activity for this user" %(self.get_activity_display())
                    raise ValidationError(message)

        return super(UserActivity, self).clean(*args, **kwargs)
