from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import requests
#import reversion
#from .. financial.models.purchase_order import PurchaseOrder
from . contacts import Contact

class ReceivingEntry(models.Model):
    asset_tag = models.CharField(default='', null=True)
    description = models.CharField(max_length=255, default='', null=True)
    date_received = models.DateField(auto_now_add=False, blank=True, null=True)
    #purchase_order = models.ForeignKey(PurchaseOrder, blank=True, null=True)
    purchased_from = models.ForeignKey(Contact)
    comments = models.CharField(max_length=255, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['date_received', ]

    def __str__(self):
        return self.asset_tag

    def get_absolute_url(self):
        return reverse("administration:fixed_asset_detail", kwargs={"pk": self.pk})
