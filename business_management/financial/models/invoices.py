from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import requests
#import reversion

from ...administration.models.contacts import Contact


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=80)
    invoice_date = models.DateField()
    company = models.CharField(max_length=60, default='optiPulse, Inc.', blank=True, null=True)
    company_address1 = models.CharField(max_length=60, default='1008 Coal Ave SE', blank=True, null=True)
    company_address2 = models.CharField(max_length=60, default='Ste. 120', blank=True, null=True)
    company_city = models.CharField(max_length=60, default='Albuquerque', blank=True, null=True)
    company_state = models.CharField(max_length=60, default='New Mexico', blank=True, null=True)
    company_zipcode = models.CharField(max_length=16, default='87106', blank=True, null=True)
    company_phone = models.CharField(max_length=24, default='888.978.4943', blank=True, null=True)

    purchased_from_company = models.ForeignKey(Contact, on_delete=models.CASCADE, limit_choices_to={'contact_type': 'VE'},)
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

    bill_to_company = models.CharField(max_length=60, default='optiPulse, Inc.', blank=True, null=True)
    bill_to_first_name = models.CharField(max_length=60, default='Caitlin', blank=True, null=True)
    bill_to_last_name = models.CharField(max_length=60, default='Marchi', blank=True, null=True)
    bill_to_email = models.CharField(max_length=80, default='billing@optipulse.com', blank=True, null=True)
    bill_to_phone = models.CharField(max_length=24, default='888.978.4943 x706', blank=True, null=True)
    bill_to_address1 = models.CharField(max_length=80, default='101 Broadway Blvd', blank=True, null=True)
    bill_to_address2 = models.CharField(max_length=80, default='Ste. 1100', blank=True, null=True)
    bill_to_city = models.CharField(max_length=80, default='Albuquerque', blank=True, null=True)
    bill_to_state = models.CharField(max_length=80, default='New Mexico', blank=True, null=True)
    bill_to_zipcode = models.CharField(max_length=80, default='87102', blank=True, null=True)

    ship_to_company = models.CharField(max_length=60, default='optiPulse, Inc.', blank=True, null=True)
    ship_to_first_name = models.CharField(max_length=60, default='Eric', blank=True, null=True)
    ship_to_last_name = models.CharField(max_length=60, default='Gieryng', blank=True, null=True)
    ship_to_email = models.CharField(max_length=80, default='info@optipulse.com', blank=True, null=True)
    ship_to_phone = models.CharField(max_length=24, default='888.978.4943 x704', blank=True, null=True)
    ship_to_address1 = models.CharField(max_length=80, default='1008 Coal Ave. SE', blank=True, null=True)
    ship_to_address2 = models.CharField(max_length=80, default='Ste. 120', blank=True, null=True)
    ship_to_city = models.CharField(max_length=80, default='Albuquerque', blank=True, null=True)
    ship_to_state = models.CharField(max_length=80, default='New Mexico', blank=True, null=True)
    ship_to_zipcode = models.CharField(max_length=80, default='87106', blank=True, null=True)

    invoice_document = models.FileField(blank=True, null=True)
    invoice_document_location = models.CharField(max_length=255, blank=True, null=True)

    comments = models.CharField(max_length=255, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['invoice_date', ]

    def __str__(self):
        inv_num = self.invoice_number
        inv_frm = self.purchased_from_company.company
        return str(inv_num + " - " + inv_frm)

    def get_absolute_url(self):
        return reverse("financial:invoice_detail", kwargs={"pk": self.pk})
