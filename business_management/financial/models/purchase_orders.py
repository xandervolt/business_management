from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import requests
#import reversion

from ...administration.models.contacts import Contact
from .invoices import Invoice


def get_po_number():
    last_po = PurchaseOrder.objects.order_by('po_number').last()
    if last_po:
        last_po_num = last_po.po_number
        new_po_num = last_po_num + 1
    else:
        new_po_num = '1'
    po_number = new_po_num
    return po_number


class PurchaseOrder(models.Model):
    po_number = models.IntegerField(unique=True, default=get_po_number)#
    po_date = models.DateField()
    invoice_number = models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=True, null=True)
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
    approved_by_doe = models.BooleanField(default=False)
    date_approved_by_doe = models.DateField(blank=True, null=True)
    approved_by_ceo = models.BooleanField(default=False)
    date_approved_by_ceo = models.DateField(blank=True, null=True)
    po_document = models.FileField(blank=True, null=True)
    po_document_location = models.CharField(max_length=255, blank=True, null=True)
    fob = models.CharField(max_length=100, default='', blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=6, decimal_places=2, default="0.00", blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    other_amount = models.DecimalField(max_digits=6, decimal_places=2, default="0.00", blank=True, null=True)
    sales_tax = models.BooleanField(default=False)
    tax_amount = models.DecimalField(max_digits=6, decimal_places=2, default="7.82", blank=True, null=True)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, default="0.00", blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default="0.00", blank=True, null=True)
    comments = models.CharField(max_length=255, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    CREDIT_CARD = 'CC'
    NET_30 = '30'
    NET_15 = '15'
    TERMS_CHOICES = (
        (CREDIT_CARD, 'Credit Card'),
        (NET_15, 'Net 15'),
        (NET_30, 'Net 30'),
    )
    terms = models.CharField(
        max_length=2,
        choices=TERMS_CHOICES,
        default=CREDIT_CARD,
    )
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


    class Meta:
        ordering = ['po_number', ]

    def __str__(self):
        return str(self.po_number)

    def get_absolute_url(self):
        return reverse("financial:purchase_order_detail", kwargs={"pk": self.pk})


class PurchaseOrderItem(models.Model):
    po_number_fk = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    qty = models.IntegerField()
    unit = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['pk', ]

    def get_absolute_url(self):
        return reverse("financial:purchase_order_detail", kwargs={"pk": self.pk})
