from django.contrib.auth.mixins import LoginRequiredMixin
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

class EngineeringDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "engineering/dashboard/dashboard.html"