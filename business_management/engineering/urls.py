from django.conf import settings
from django.conf.urls import include, url
from .views import dashboard
from .views import products


urlpatterns = [
    url(r'^$', dashboard.EngineeringDashboardView.as_view(), name='engineering'),
    url(r'^products/', products.ProductListView.as_view(), name='product_list'),
]