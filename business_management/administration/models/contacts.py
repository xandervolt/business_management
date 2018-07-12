from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import requests
#import reversion

class Contact(models.Model):
    first_name = models.CharField(max_length=60, default='', blank=True, null=True)
    last_name = models.CharField(max_length=60, default='', blank=True, null=True)
    company = models.CharField(max_length=60, default='', blank=True, null=True)
    phone_number = models.CharField(max_length=60, default='', blank=True, null=True)
    mobile_number = models.CharField(max_length=60, default='', blank=True, null=True)
    fax_number = models.CharField(max_length=60, default='', blank=True, null=True)
    address1 = models.CharField(max_length=100, default='', blank=True, null=True)
    address2 = models.CharField(max_length=60, default='', blank=True, null=True)
    city = models.CharField(max_length=60, default='', blank=True, null=True)
    state = models.CharField(max_length=30, default='', blank=True, null=True)
    zipcode = models.CharField(max_length=18, default='', blank=True, null=True)
    country = models.CharField(max_length=60, default='', blank=True, null=True)
    email = models.EmailField(max_length=60)

    VENDOR = 'VE'
    CONTRACTOR = 'CO'
    POTENTIAL_CUSTOMER ='PC'
    POTENTIAL_INVESTOR ='PI'
    CUSTOMER ='CU'
    INVESTOR ='IN'
    PARTNER = 'PA'
    OTHER ='OT'
    CONTACT_TYPE_CHOICES = (
        (VENDOR, 'Vendor'),
        (CONTRACTOR, 'Contractor'),
        (POTENTIAL_CUSTOMER, 'Potential Customer'),
        (POTENTIAL_INVESTOR, 'Potential Investor'),
        (CUSTOMER, 'Customer'),
        (INVESTOR, 'Investor'),
        (PARTNER, 'Partner'),
        (OTHER, 'Other'),
    )
    contact_type = models.CharField(
        max_length=2,
        choices=CONTACT_TYPE_CHOICES,
    )

    comments = models.CharField(max_length=255, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("administration:contact_detail", kwargs={"pk": self.pk})
