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
from ..models.laser_masks import LaserMask
from ..mixins import FileUploadMixin

# Create your views here.

class LaserMaskListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'engineering.view_laser_mask'
    login_url = 'accounts:access_denied'
    context_object_name = "laser_masks"
    model = LaserMask
    template_name = 'engineering/laser_masks/laser_mask_list.html'
    queryset = LaserMask.objects.filter(in_trash=False)

class LaserMaskDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'engineering.view_laser_mask'
    login_url = 'accounts:access_denied'
    model = LaserMask
    template_name = 'engineering/laser_masks/laser_mask_detail.html'

class LaserMaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, FileUploadMixin, CreateView):
    permission_required = 'engineering.add_laser_mask'
    login_url = 'accounts:access_denied'
    fields = ("laser_mask_ui", "mask_layer", "mask_design", "fab_date", "fab_vendor", "notes")
    model = LaserMask
    template_name = 'engineering/laser_masks/laser_mask_form.html'
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(LaserMaskCreateView, self).form_valid(form)
    
class LaserMaskUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'engineering.change_laser_mask'
    login_url = 'accounts:access_denied'
    fields = ("laser_mask_ui", "mask_layer", "mask_design", "fab_date", "fab_vendor", "notes")
    model = LaserMask
    template_name = 'engineering/laser_masks/laser_mask_form.html'
    
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.laser_mask_ui)