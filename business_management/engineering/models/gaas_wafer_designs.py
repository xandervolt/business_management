import os, datetime
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import reversion

def upload_path(instance, filename):
    return os.path.join('uploads/' + datetime.datetime.now().strftime('%Y/%m/%d/') + instance.design_ui, filename)

# Create your models here.
@reversion.register
class GaasWaferDesign(models.Model):
    design_ui = models.CharField(max_length=60, unique=True) # Wafer Design UI

    TOP_EMITTING = 'TE'
    BOTTOM_EMITTING = 'BE'

    EMITTING_CHOICES = (
        (TOP_EMITTING, 'Top-Emitting'),
        (BOTTOM_EMITTING, 'Bottom-Emitting'),
    )
    emitting = models.CharField(
        max_length=2,
        choices=EMITTING_CHOICES,
        default=TOP_EMITTING,
    )

    contact_location = models.CharField(max_length=255, default='')
    optical_power = models.DecimalField(max_digits=20, decimal_places=4, default=0.0000)
    design_date = models.DateTimeField()
    designer = models.CharField(max_length=255, default='')
    designer_ui = models.CharField(max_length=255, default='', blank=True)
    design_document = models.FileField(upload_to=upload_path, blank=True)
    notes = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    in_trash = models.BooleanField(default=False)
    inactive_date = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        ordering = ['design_ui', ]

    def __str__(self):
        return self.design_ui

    def get_absolute_url(self):
        return reverse("engineering:gaas_wafer_design_detail", kwargs={"pk": self.pk})
