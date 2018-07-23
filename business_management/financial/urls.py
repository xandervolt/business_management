from django.conf import settings
from django.conf.urls import include, url

from .views import purchase_orders

urlpatterns = [
    url(r'^purchase_orders/create/$', purchase_orders.PurchaseOrderCreateView.as_view(), name='purchase_order_create'),
    url(r'^purchase_orders/$', purchase_orders.PurchaseOrderListView.as_view(), name='purchase_order_list'),
    #url(r'^$', purchase_orders.PurchaseOrderUpdateView.as_view(), name='purchase_order_update'),
    url(r'^purchase_orders/(?P<pk>\d+)/$', purchase_orders.PurchaseOrderDetailView.as_view(), name='purchase_order_detail'),
]
