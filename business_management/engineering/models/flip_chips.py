from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

#from .flip_chips.models import FlipChip

# Create your models here.
class FlipChip(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    in_trash = models.BooleanField(default=False)
    serial_num = models.CharField(max_length=255)
    #laser_chip = models.ForeignKey(LaserChip)
    #substrate = models.ForeignKey(Substrate)
    notes = models.TextField(blank=True, default='')
    bond_date = models.DateTimeField()
    
    class Meta:
        ordering = ['serial_num', ]
    
    def __str__(self):
        return self.serial_num
    
    def get_absolute_url(self):
        return reverse("engineering:flip_chips:detail", kwargs={"pk": self.pk})