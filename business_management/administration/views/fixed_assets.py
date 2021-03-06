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
from ..models.fixed_assets import FixedAsset

# Create your views here.

class FixedAssetListView(LoginRequiredMixin, ListView):
    context_object_name = "fixed_assets"
    model = FixedAsset
    template_name = 'administration/fixed_assets/fixed_asset_list.html'

    def get_queryset(self):
        return self.model.objects.filter(active=True)


class FixedAssetInactiveListView(LoginRequiredMixin, ListView):
    context_object_name = "fixed_assets"
    model = FixedAsset
    template_name = 'administration/fixed_assets/fixed_asset_inactive_list.html'

    def get_queryset(self):
        return self.model.objects.filter(active=False)


class FixedAsset500ListView(LoginRequiredMixin, ListView):
    context_object_name = "fixed_assets"
    model = FixedAsset
    template_name = 'administration/fixed_assets/fixed_asset_500_list.html'

    def get_queryset(self):
        return self.model.objects.filter(purchase_price__gte=500)


class FixedAsset1000ListView(LoginRequiredMixin, ListView):
    context_object_name = "fixed_assets"
    model = FixedAsset
    template_name = 'administration/fixed_assets/fixed_asset_1000_list.html'

    def get_queryset(self):
        return self.model.objects.filter(purchase_price__gte=1000)


class FixedAssetDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "fixed_asset"
    model = FixedAsset
    template_name = 'administration/fixed_assets/fixed_asset_detail.html'


class FixedAssetCreateView(LoginRequiredMixin, CreateView):
    fields = ("asset_tag", "serial_number", "manufacturer", "model_number", "description", "purchase_date", "purchase_price", "purchased_from", "purchase_condition", "asset_type", "owner", "location", "active", "inactive_date", "comments")
    model = FixedAsset
    template_name = 'administration/fixed_assets/fixed_asset_form.html'
    #form = forms.CreateProductForm()

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(FixedAssetCreateView, self).form_valid(form)


class FixedAssetUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("asset_tag", "serial_number", "manufacturer", "model_number", "description", "purchase_date", "purchase_price", "purchased_from", "purchase_condition", "asset_type", "owner", "location", "active", "inactive_date", "comments")
    model = FixedAsset
    template_name = 'administration/fixed_assets/fixed_asset_form.html'

    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.serial_num)
