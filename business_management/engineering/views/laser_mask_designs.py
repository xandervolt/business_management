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
from ..mixins import FileUploadMixin


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

class LaserMaskDesignCreateView(LoginRequiredMixin, PermissionRequiredMixin, FileUploadMixin, CreateView):
    permission_required = 'engineering.add_laser_mask_design'
    login_url = 'accounts:access_denied'
    fields = ("laser_mask_design_ui", "mask_layers", "design_date", "designer", "pcm", "critical_dimensions", "dimensions", "thickness", "thickness", "material", "number_of_products", "chip_list", "design_document", "notes")
    model = LaserMaskDesign
    template_name = 'engineering/laser_mask_designs/laser_mask_design_form.html'

    '''
    def handle_file_upload(design_document):
    
        # Get the authenticated user credentials from python-social-auth
        social = request.user.social_auth.get(provider='office365')
        access_token = social.extra_data['access_token']
    
        # build our header for the api call
        headers = {
            'Authorization' : 'Bearer {0}'.format(access_token),
        }
    
        # build the url for the api call
        # Look at https://dev.onedrive.com/items/upload_put.htm for reference
        url = 'https://36b2a01a-c6af-4694-bb6c-c941c1ec8b4a.sharepoint.com/sites/{site-id}/drive/items/{parent-id}:/' + design_document + ':/content'
        # Make the api call
        response = requests.put(url, data=open(design_document, 'rb'), headers=headers)
        return response 
    '''
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(LaserMaskDesignDetailView, self).form_valid(form)
    
class LaserMaskDesignUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'engineering.change_laser_mask_design'
    login_url = 'accounts:access_denied'
    fields = ("mask_layers", "design_date", "designer", "pcm", "critical_dimensions", "dimensions", "thickness", "thickness", "material", "number_of_products", "chip_list", "design_document", "notes")
    model = LaserMaskDesign
    template_name = 'engineering/laser_mask_designs/laser_mask_design_form.html'
    
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.laser_mask_design_ui)