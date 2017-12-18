from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
#import reversion

# Create your models here.
#@reversion.register
class LaserMaskDesign(models.Model):
    laser_mask_design_ui = models.CharField(max_length=60, unique=True) # Wafer Design UI
    mask_layers = models.CharField(max_length=255, default='')
    design_date = models.DateTimeField()
    designer = models.CharField(max_length=255, default='')
    pcm = models.CharField(max_length=255, default='')
    critical_dimensions = models.DecimalField(max_digits=20, decimal_places=4, default=0.0000)
    dimensions = models.CharField(max_length=255, default='')
    thickness = models.DecimalField(max_digits=20, decimal_places=4, default=0.0000)
    material = models.CharField(max_length=255, default='')
    number_of_products = models.IntegerField(default=0)
    chip_list = models.CharField(max_length=255, default='')
    design_document = models.FileField(upload_to='uploads/%Y/%m/%d/')
    notes = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    in_trash = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['laser_mask_design_ui', ]
    
    def __str__(self):
        return self.laser_mask_design_ui
    
    def get_absolute_url(self):
        return reverse("engineering:laser_mask_design_detail", kwargs={"pk": self.pk})
    