from django.contrib import admin

# Register your models here.
from .models.fixed_assets import FixedAsset

admin.site.register(FixedAsset)
