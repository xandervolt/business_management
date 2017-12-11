from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

#from .flip_chips.models import FlipChip

# Create your models here.
class LaserChip(models.Model):
    serial_num = models.CharField(max_length=255)
    #laser_chip = models.ForeignKey(LaserChip)
    #substrate = models.ForeignKey(Substrate) 
    bond_pressure = models.DecimalField(max_digits=20, decimal_places=4, default=0.0000)
    bond_heat = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    bond_time = models.DecimalField(max_digits=10, decimal_places=4, default=0.0000)
    bond_date = models.DateTimeField()
    bond_tool = models.CharField(max_length=255, default='')
    carrier = models.CharField(max_length=255, default='')
    geo_location = models.CharField(max_length=255, default='')
    notes = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    in_trash = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['serial_num', ]
    
    def __str__(self):
        return self.serial_num
    
    def get_absolute_url(self):
        return reverse("engineering:flip_chips:detail", kwargs={"pk": self.pk})