from django import forms
from .models.fixedassets import FixedAsset

class FixedAssetForm(forms.ModelForm):
    class Meta:
        model = FixedAsset
        fields = ('asset_tag', 'serial_number', 'manufacturer', 'model_number', )
