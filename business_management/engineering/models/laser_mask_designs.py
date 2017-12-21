from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import requests
#import reversion

# Create your models here.
#@reversion.register
class LaserMaskDesign(models.Model):
    laser_mask_design_ui = models.CharField(max_length=60, unique=True) # Wafer Design UI
    mask_layers = models.CharField(max_length=255, default='', blank=True, null=True)
    design_date = models.DateTimeField(blank=True, null=True)
    designer = models.CharField(max_length=255, default='', blank=True, null=True)
    pcm = models.CharField(max_length=255, default='', blank=True, null=True)
    critical_dimensions = models.DecimalField(max_digits=20, decimal_places=4, default=0.0000, blank=True, null=True)
    dimensions = models.CharField(max_length=255, default='')
    thickness = models.DecimalField(max_digits=20, decimal_places=4, default=0.0000, blank=True, null=True)
    material = models.CharField(max_length=255, default='', blank=True, null=True)
    number_of_products = models.IntegerField(default=0, blank=True, null=True)
    chip_list = models.CharField(max_length=255, default='', blank=True, null=True)
    design_document = models.FileField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    in_trash = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
         # Get the authenticated user credentials from python-social-auth
        social = request.user.allauth.get(provider='office365')
        access_token = social.extra_data['access_token']
    
        # build our header for the api call
        headers = {
            'Authorization' : 'Bearer {0}'.format(access_token),
        }
    
        # build the url for the api call
        # Look at https://dev.onedrive.com/items/upload_put.htm for reference
        url = 'https://graph.microsoft.com/v1.0/me/'
        #url = 'https://graph.microsoft.com/v1.0/sites/ITSupport/drive/root:/' + self.design_document.name + ':/content'
        # Make the api call
        response = requests.get(url)
        #response = requests.put(url, data=open(self.design_document, 'rb'), headers=headers)
        #return response
    
        super(LaserMaskDesign, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['laser_mask_design_ui', ]
    
    def __str__(self):
        return self.laser_mask_design_ui
    
    def get_absolute_url(self):
        return reverse("engineering:laser_mask_design_detail", kwargs={"pk": self.pk})
    