from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)


# Create your views here.

class EngineeringDashboardView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "engineering/dashboard/dashboard.html"
    permission_required = 'engineering.view_product'
    login_url = 'accounts:access_denied'
    
class DatabaseFlowView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "engineering/database_flow/database_flow.html"
    permission_required = 'engineering.view_product'
    login_url = 'accounts:access_denied'