from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from braces.views import GroupRequiredMixin
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
from ..models.products import Product

# Create your views here.

class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'engineering.change_product'
    login_url = 'accounts:logout'
    permission_denied_message = 'Nope'
    context_object_name = "products"
    model = Product
    template_name = 'engineering/products/product_list.html'

class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'engineering.view_product'
    raise_exception = True
    model = Product
    
    
class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'engineering.add_product'
    raise_exception = True
    fields = ("serial_num", "build_date", "created_by", "notes")
    model = Product
    #form = forms.CreateProductForm()
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(ProductCreateView, self).form_valid(form)
    
    
class ProductUpdateView(LoginRequiredMixin,  PermissionRequiredMixin, UpdateView):
    permission_required = 'engineering.change_product'
    raise_exception = True
    fields = ("serial_num", "build_date", "notes")
    model = Product
    
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.serial_num)