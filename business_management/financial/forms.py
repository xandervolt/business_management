from importlib import import_module
from django import forms

from .models.purchase_orders import PurchaseOrder


class PurchaseOrderForm(forms.ModelForm):

    class Meta:
        model = PurchaseOrder
        #fields = '__all__'
        exclude = ['created_by']
