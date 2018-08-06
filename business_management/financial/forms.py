from importlib import import_module
from django import forms

from .models.purchase_orders import PurchaseOrder, PurchaseOrderItem
from .models.invoices import Invoice


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        #fields = '__all__'
        exclude = ['created_by']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        #fields = '__all__'
        exclude = ['created_by']

class PurchaseOrderItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'
