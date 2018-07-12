from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import requests
#import reversion

from .. administration.models.contacts import Contact

class PurchaseOrder(models.Model):
    po_number = models.IntegerField(max_length=8, unique=True)
    po_date = models.DateField()
    company = models.CharField(max_length=60, default='optiPulse, Inc.')
    company_address = models.CharField(max_length=60, default='1008 Coal Ave SE, Ste. 120')
    company_city = models.CharField(max_length=60, default='Albuquerque')
    company_state = models.CharField(max_length=60, default='New Mexico')
    company_zipcode = models.CharField(max_length=16, default='87106')
    company_phone = models.CharField(max_length=24, default='888.978.4943')
    purchased_from_company = models.ForeignKey(Contact, related_name='company')
    purchased_from_first_name = models.CharField(max_length=80, blank=True, null=True)
    purchased_from_last_name = models.CharField(max_length=80, blank=True, null=True)
    purchased_from_address1 = models.CharField(max_length=80, blank=True, null=True)
    purchased_from_address2 = models.CharField(max_length=80, blank=True, null=True)
    purchased_from_phone = models.CharField(max_length=24, blank=True, null=True)
    purchased_from_fax = models.CharField(max_length=24, blank=True, null=True)
    purchased_from_email = models.EmailField(max_length=80, blank=True, null=True)
    purchased_from_address1 = models.CharField(max_length=80, blank=True, null=True)
    purchased_from_address2 = models.CharField(max_length=80, blank=True, null=True)
    purchased_from_city = models.CharField(max_length=80, blank=True, null=True)
    purchased_from_state = models.CharField(max_length=80, blank=True, null=True)
    purchased_from_zip = models.CharField(max_length=80, blank=True, null=True)
    purchased_from_country = models.CharField(max_length=80, blank=True, null=True)
    bill_to_company = models.CharField(max_length=60, blank=True, null=True)
    bill_to_first_name = models.CharField(max_length=60, blank=True, null=True)
    bill_to_last_name = models.CharField(max_length=60, blank=True, null=True)
    bill_to_email = models.CharField(max_length=80, blank=True, null=True)
    bill_to_phone = models.CharField(max_length=24, blank=True, null=True)
    bill_to_address1 = models.CharField(max_length=80, blank=True, null=True)
    bill_to_address2 = models.CharField(max_length=80, blank=True, null=True)
    approved_by_doe = models.BooleanField(default=False)
    date_approved_by_doe = models.DateField(default='', blank=True, null=True)
    approved_by_ceo = models.BooleanField(default=False)
    date_approved_by_ceo = models.DateField(default='', blank=True, null=True)

    CREDIT_CARD = 'CC'
    NET_30 = '30'
    TERMS_CHOICES = (
        (CREDIT_CARD, 'Credit Card'),
        (NET_30, 'Net 30'),
    )
    terms = models.CharField(
        max_length=2,
        choices=TERMS_CHOICES,
        default=CREDIT_CARD,
    )

    fob = models.CharField(max_length=100, default='', blank=True, null=True)

    FED_EX_ACCT = 'FE'
    VENDOR = 'VE'
    EXTRA = 'EX'
    SHIPPING_CHOICES = (
        (FED_EX_ACCT, 'optiPulse FedEX Account'),
        (VENDOR, 'Paid by Vendor'),
        (EXTRA, 'Additional Charge'),
    )
    shipping = models.CharField(
        max_length=2,
        choices=SHIPPING_CHOICES,
        default=FED_EX_ACCT,
    )

    comments = models.CharField(max_length=255, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['po_number', ]

    def __str__(self):
        return self.po_number

    def get_absolute_url(self):
        return reverse("financial:purchase_order_detail", kwargs={"pk": self.pk})
