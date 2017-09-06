from django.conf import settings
from django.conf.urls import include, url
from .views import dashboard

urlpatterns = [
    url(r'^$', dashboard.EngineeringDashboardView.as_view(), name='engineering'),
]