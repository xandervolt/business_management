from django.conf import settings
from django.conf.urls import include, url
from .views import fixed_assets

urlpatterns = [
    url(r'^fixed_assets/$', fixed_assets.FixedAssetListView.as_view(), name='fixed_asset_list'),
    url(r'^fixed_assets/create/$', fixed_assets.FixedAssetCreateView.as_view(), name='fixed_asset_create'),
    url(r'^fixed_assets/edit/(?P<pk>\d+)/$', fixed_assets.FixedAssetUpdateView.as_view(), name='fixed_asset_update'),
    url(r'^fixed_assets/(?P<pk>\d+)/$', fixed_assets.FixedAssetDetailView.as_view(), name='fixed_asset_detail'),
]
