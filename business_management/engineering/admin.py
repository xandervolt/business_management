from django.contrib import admin

# Register your models here.
from .models.gaas_wafer_designs import GaasWaferDesign

admin.site.register(GaasWaferDesign)