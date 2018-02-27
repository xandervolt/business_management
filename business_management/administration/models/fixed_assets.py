from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import requests
#import reversion

class FixedAsset(models.Model):
    asset_tag = models.CharField(max_length=20, unique=True)
    serial_number = models.CharField(max_length=100, default='', blank=True, null=True)
    manufacturer = models.CharField(max_length=100, default='', null=True)
    model_number = models.CharField(max_length=100, default='', null=True)
    purchase_date = models.DateField(auto_now_add=False)
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2, default=000000.00, blank=True, null=True)
    purchased_from = models.CharField(max_length=100, default='', blank=True, null=True)

    NEW = 'NE'
    USED = 'US'
    REFURBISHED ='RE'
    MANUFACTURER_REFURBISHED ='MR'
    PURCHASE_CONDITION_CHOICES = (
        (NEW, 'New'),
        (USED, 'Used'),
        (MANUFACTURER_REFURBISHED, 'Manufacturer Refurbished'),
        (REFURBISHED, 'Refurbished'),
    )
    purchase_condition = models.CharField(
        max_length=2,
        choices=PURCHASE_CONDITION_CHOICES,
        default=NEW,
    )

    active = models.BooleanField(default=True)
    inactive_date = models.DateField(auto_now_add=False, null=True, blank=True)

    COMPUTER_EQUIPMENT = 'CE'
    LAB_EQUIPMENT = 'LE'
    FURNITURE = 'FU'
    SOFTWARE = 'SO'
    OFFICE_EQUIPMENT = 'OE'
    ASSET_TYPE_CHOICES = (
        (COMPUTER_EQUIPMENT, 'Computer Equipment'),
        (OFFICE_EQUIPMENT, 'Office Equipment'),
        (LAB_EQUIPMENT, 'Lab Equipment'),
        (FURNITURE, 'Furniture'),
        (SOFTWARE, 'Software'),
    )
    asset_type = models.CharField(
        max_length=2,
        choices=ASSET_TYPE_CHOICES,
        default=COMPUTER_EQUIPMENT,
    )

    location = models.CharField(max_length=100, default='', blank=True, null=True)
    owner = models.CharField(max_length=100, default='', blank=True, null=True)
    comments = models.CharField(max_length=255, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['purchase_date', ]

    def __str__(self):
        return self.asset_tag

    def get_absolute_url(self):
        return reverse("administration:fixed_asset_detail", kwargs={"pk": self.pk})
