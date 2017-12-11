from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from .gaas_wafer_designs import GaasWaferDesign

# Create your models here.
class GaasWafer(models.Model):
    wafer_ui = models.CharField(max_length=60, unique=True) # Wafer Design UI
    wafer_design = models.ForeignKey(GaasWaferDesign)
    growth_date = models.DateTimeField()
    wafer_position = models.CharField(max_length=255, default='')
    reflectance_map = models.CharField(max_length=255, default='')
    wafer_diameter = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    conductivity = models.DecimalField(max_digits=10, decimal_places=4, default=0.0000)
    vendor = models.CharField(max_length=255, default='')
    wafer_growth_lot = models.CharField(max_length=255, default='')
    wavelength = models.DecimalField(max_digits=10, decimal_places=4, default=0.0000)
    gain_offset = models.DecimalField(max_digits=10, decimal_places=4, default=0.0000)
    designed_operating_temp = models.DecimalField(max_digits=10, decimal_places=4, default=0.0000)
    notes = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    in_trash = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['wafer_ui', ]
    
    def __str__(self):
        return self.wafer_ui
    
    def get_absolute_url(self):
        return reverse("engineering:gaas_wafer_detail", kwargs={"pk": self.pk})
    