from django.conf import settings
from django.conf.urls import include, url
from .views import dashboard
from .views import products
from .views import flip_chips


urlpatterns = [
    url(r'^$', dashboard.EngineeringDashboardView.as_view(), name='engineering'),
    url(r'^products/', products.ProductListView.as_view(), name='product_list'),
    url(r'^flip-chips/', flip_chips.FlipChipListView.as_view(), name='flip_chip_list'),
]