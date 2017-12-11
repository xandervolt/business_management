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
from ..models.gaas_wafers import GaasWafer

# Create your views here.

class GaasWaferListView(LoginRequiredMixin, ListView):
    context_object_name = "gaas_wafers"
    model = GaasWafer
    template_name = 'engineering/gaas_wafers/gaas_wafer_list.html'

class GaasWaferDetailView(LoginRequiredMixin, DetailView):
    model = GaasWafer
    template_name = 'engineering/gaas_wafers/gaas_wafer_detail.html'

class GaasWaferCreateView(LoginRequiredMixin, CreateView):
    fields = ("wafer_ui",  "notes")
    model = GaasWafer
    template_name = 'engineering/gaas_wafers/gaas_wafer_form.html'
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(GaasWaferCreateView, self).form_valid(form)
    
class GaasWaferUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("wafer_ui",  "notes")
    model = GaasWafer
    template_name = 'engineering/gaas_wafers/gaas_wafer_form.html'
    
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.wafer_ui)