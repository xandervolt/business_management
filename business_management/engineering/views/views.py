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
    
'''
class ProductListView(LoginRequiredMixin, ListView):
    context_object_name = "products"
    model = Product
    

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    fields = ("serial_num", "build_date", "created_by", "notes")
    model = Product
    #form = forms.CreateProductForm()
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(ProductCreateView, self).form_valid(form)
    
    
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("serial_num", "build_date", "notes")
    model = Product
    
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.serial_num)
'''