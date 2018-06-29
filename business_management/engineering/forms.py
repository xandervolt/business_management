from importlib import import_module
from django import forms

from .models.gaas_wafer_designs import GaasWaferDesign


class GaasWaferDesignForm(forms.ModelForm):

    class Meta:
        model = GaasWaferDesign
        exclude = ['created_by',]
