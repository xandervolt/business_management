from django.contrib import admin

# Register your models here.
from .models.invoices import Invoice
from .models.purchase_orders import PurchaseOrder

admin.site.register(Invoice)
admin.site.register(PurchaseOrder)
