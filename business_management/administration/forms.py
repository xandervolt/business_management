from django import forms
from .models.fixed_assets import FixedAsset
from .models.contacts import Contact
#from .models.timesheets import ClockPunch

class FixedAssetForm(forms.ModelForm):
    class Meta:
        model = FixedAsset
        fields = ('asset_tag', 'serial_number', 'manufacturer', 'model_number', )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['created_by', 'created_at']
