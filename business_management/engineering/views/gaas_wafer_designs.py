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
from ..models.gaas_wafer_designs import GaasWaferDesign

# Create your views here.

class GaasWaferDesignListView(LoginRequiredMixin, ListView):
    context_object_name = "gaas_wafer_designs"
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_list.html'

class GaasWaferDesignDetailView(LoginRequiredMixin, DetailView):
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_detail.html'

class GaasWaferDesignCreateView(LoginRequiredMixin, CreateView):
    fields = ("design_ui", "emitting", "contact_location", "optical_power", "design_date", "designer", "design_ui", "notes")
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form.html'
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(GaasWaferDesignCreateView, self).form_valid(form)
    
    
class GaasWaferDesignUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("design_ui", "emitting", "contact_location", "optical_power", "design_date", "designer", "design_ui", "notes")
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form.html'
    
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.design_ui)