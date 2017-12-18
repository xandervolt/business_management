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
from ..models.laser_mask_designs import LaserMaskDesign

# Create your views here.

class LaserMaskDesignListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'engineering.view_laser_mask_design'
    login_url = 'accounts:access_denied'
    context_object_name = "laser_mask_designs"
    model = LaserMaskDesign
    template_name = 'engineering/laser_mask_designs/laser_mask_design_list.html'

class LaserMaskDesignDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'engineering.view_laser_mask_design'
    login_url = 'accounts:access_denied'
    model = LaserMaskDesign
    template_name = 'engineering/laser_mask_designs/laser_mask_design_detail.html'

class LaserMaskDesignCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'engineering.view_laser_mask_design'
    login_url = 'accounts:access_denied'
    fields = ("laser_mask_design_ui", "mask_layers", "design_date", "designer", "pcm", "critical_dimensions", "dimensions", "thickness", "thickness", "material", "number_of_products", "chip_list", "design_document", "notes")
    model = LaserMaskDesign
    template_name = 'engineering/laser_mask_designs/laser_mask_design_form.html'
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(LaserMaskDesignCreateView, self).form_valid(form)
    
class LaserMaskDesignUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'engineering.view_laser_mask_design'
    login_url = 'accounts:access_denied'
    fields = ("mask_layers", "design_date", "designer", "pcm", "critical_dimensions", "dimensions", "thickness", "thickness", "material", "number_of_products", "chip_list", "design_document", "notes")
    model = LaserMaskDesign
    template_name = 'engineering/laser_mask_designs/laser_mask_design_form.html'
    
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.laser_mask_design_ui)