from django.conf import settings
from django.conf.urls import include, url

from .views import purchase_orders, invoices

urlpatterns = [
    # Purchase Orders
    url(r'^purchase-orders/create/$', purchase_orders.PurchaseOrderCreateView.as_view(), name='purchase_order_create'),
    url(r'^purchase-orders/$', purchase_orders.PurchaseOrderListView.as_view(), name='purchase_order_list'),
    #url(r'^$', purchase_orders.PurchaseOrderUpdateView.as_view(), name='purchase_order_update'),
    url(r'^purchase-orders/(?P<pk>\d+)/$', purchase_orders.PurchaseOrderDetailView.as_view(), name='purchase_order_detail'),

    url(r'^purchase-order-items/create/(?P<pk>\d+)/$', purchase_orders.PurchaseOrderItemCreateView.as_view(), name='purchase_order_item_create'),

    # Invoices
    url(r'^invoices/create/$', invoices.InvoiceCreateView.as_view(), name='invoice_create'),
    url(r'^invoices/$', invoices.InvoiceListView.as_view(), name='invoice_list'),
    #url(r'^$', purchase_orders.PurchaseOrderUpdateView.as_view(), name='purchase_order_update'),
    url(r'^invoices/(?P<pk>\d+)/$', invoices.InvoiceDetailView.as_view(), name='invoice_detail'),
]
