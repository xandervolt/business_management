from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from .laser_mask_designs import LaserMaskDesign
#import reversion

# Create your models here.
#@reversion.register
class LaserMask(models.Model):
    laser_mask_ui = models.CharField(max_length=60, unique=True) # Wafer Design UI
    mask_layer = models.CharField(max_length=255, default='')
    mask_design = models.ForeignKey(LaserMaskDesign)
    fab_date = models.DateTimeField()
    fab_vendor = models.CharField(max_length=255, default='')
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    notes = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    in_trash = models.BooleanField(default=False)

    class Meta:
        ordering = ['laser_mask_ui', ]

    def __str__(self):
        return self.laser_mask_ui

    def get_absolute_url(self):
        return reverse("engineering:laser_mask_detail", kwargs={"pk": self.pk})
