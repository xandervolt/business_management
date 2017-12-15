from django.conf import settings
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^access-denied/$', views.AccessDeniedView.as_view(), name='access_denied'),
]