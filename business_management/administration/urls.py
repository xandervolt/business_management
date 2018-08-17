from django.conf import settings
from django.conf.urls import include, url
from .views import fixed_assets, contacts, timesheets

urlpatterns = [
    url(r'^fixed_assets/$', fixed_assets.FixedAssetListView.as_view(), name='fixed_asset_list'),
    url(r'^fixed_assets/over500/$', fixed_assets.FixedAsset500ListView.as_view(), name='fixed_asset_500_list'),
    url(r'^fixed_assets/over1000/$', fixed_assets.FixedAsset1000ListView.as_view(), name='fixed_asset_1000_list'),
    url(r'^fixed_assets/inactive/$', fixed_assets.FixedAssetInactiveListView.as_view(), name='fixed_asset_inactive_list'),
    url(r'^fixed_assets/create/$', fixed_assets.FixedAssetCreateView.as_view(), name='fixed_asset_create'),
    url(r'^fixed_assets/edit/(?P<pk>\d+)/$', fixed_assets.FixedAssetUpdateView.as_view(), name='fixed_asset_update'),
    url(r'^fixed_assets/(?P<pk>\d+)/$', fixed_assets.FixedAssetDetailView.as_view(), name='fixed_asset_detail'),

    #url(r'^timesheets/$', employees.TimesheetListView.as_view(), name='timesheet_list'),

    #url(r'^timesheets/clock-out/$', timesheets.ClockPunchOutView.as_view(), name='clock_out'),
    #url(r'^timesheets/clock-in/$', timesheets.ClockPunchInView.as_view(), name='clock_in'),

    url(r'^contacts/$', contacts.ContactListView.as_view(), name='contact_list'),
    url(r'^contacts/create$', contacts.ContactCreateView.as_view(), name='contact_create'),
]
