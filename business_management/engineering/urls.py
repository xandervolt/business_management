from django.conf import settings
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.EngineeringDashboardView.as_view(), name='engineering'),
]