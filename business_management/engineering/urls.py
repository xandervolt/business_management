from django.conf import settings
from django.conf.urls import include, url
from .views import dashboard
from .views import products
from .views import flip_chips
from .views import gaas_wafer_designs
from .views import gaas_wafers
from .views import laser_mask_designs
from .views import laser_masks


urlpatterns = [
    url(r'^$', dashboard.EngineeringDashboardView.as_view(), name='engineering'),
    url(r'^database-flow/$', dashboard.DatabaseFlowView.as_view(), name='database_flow'),

    url(r'^products/$', products.ProductListView.as_view(), name='product_list'),
    url(r'^flip-chips/$', flip_chips.FlipChipListView.as_view(), name='flip_chip_list'),

    # GaAs Wafer Designs URLS
    url(r'^gaas-wafer-designs/$', gaas_wafer_designs.GaasWaferDesignListView.as_view(), name='gaas_wafer_design_list'),
    url(r'^gaas-wafer-designs/create/$', gaas_wafer_designs.GaasWaferDesignFormView.as_view(), name='gaas_wafer_design_create'),
    #url(r'^gaas-wafer-designs/create/$', gaas_wafer_designs.GaasWaferDesignCreateView.as_view(), name='gaas_wafer_design_create'),
    #url(r'^gaas-wafer-designs/create/$', gaas_wafer_designs.gaas_create, name='gaas_wafer_design_create'),
    url(r'^gaas-wafer-designs/edit/(?P<pk>\d+)/$', gaas_wafer_designs.GaasWaferDesignUpdateView.as_view(), name='gaas_wafer_design_update'),
    url(r'^gaas-wafer-designs/(?P<pk>\d+)/$', gaas_wafer_designs.GaasWaferDesignDetailView.as_view(), name='gaas_wafer_design_detail'),

    # GaAs Wafers URLS
    url(r'^gaas-wafers/$', gaas_wafers.GaasWaferListView.as_view(), name='gaas_wafer_list'),
    url(r'^gaas-wafers/create/$', gaas_wafers.GaasWaferCreateView.as_view(), name='gaas_wafer_create'),
    url(r'^gaas-wafers/edit/(?P<pk>\d+)/$', gaas_wafers.GaasWaferUpdateView.as_view(), name='gaas_wafer_update'),
    url(r'^gaas-wafers/(?P<pk>\d+)/$', gaas_wafers.GaasWaferDetailView.as_view(), name='gaas_wafer_detail'),

    # Laser Mask Designs URLS
    url(r'^laser-mask-designs/$', laser_mask_designs.LaserMaskDesignListView.as_view(), name='laser_mask_design_list'),
    url(r'^laser-mask-designs/create/$', laser_mask_designs.LaserMaskDesignCreateView.as_view(), name='laser_mask_design_create'),
    url(r'^laser-mask-designs/edit/(?P<pk>\d+)/$', laser_mask_designs.LaserMaskDesignUpdateView.as_view(), name='laser_mask_design_update'),
    url(r'^laser-mask-designs/(?P<pk>\d+)/$', laser_mask_designs.LaserMaskDesignDetailView.as_view(), name='laser_mask_design_detail'),

    # Laser Masks URLS
    url(r'^laser-masks/$', laser_masks.LaserMaskListView.as_view(), name='laser_mask_list'),
    url(r'^laser-masks/create/$', laser_masks.LaserMaskCreateView.as_view(), name='laser_mask_create'),
    url(r'^laser-masks/edit/(?P<pk>\d+)/$', laser_masks.LaserMaskUpdateView.as_view(), name='laser_mask_update'),
    url(r'^laser-masks/(?P<pk>\d+)/$', laser_masks.LaserMaskDetailView.as_view(), name='laser_mask_detail'),
]
