from django.conf import settings
from django.conf.urls import url
#from .views import dashboard
#from .views import products
#from .views import flip_chips
from ..views import gaas_wafer_designs

urlpatterns = [
    url(r'^$', gaas_wafer_designs.GaasWaferDesignListView.as_view(), name='list'),
    url(r'^create/$', gaas_wafer_designs.GaasWaferDesignCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', gaas_wafer_designs.GaasWaferDesignUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$', gaas_wafer_designs.GaasWaferDesignDetailView.as_view(), name='detail'),
]