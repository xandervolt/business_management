from django.contrib import admin

# Register your models here.
from .models.fixed_assets import FixedAsset
from .models.contacts import Contact

admin.site.register(FixedAsset)
admin.site.register(Contact)
