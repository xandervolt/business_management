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
from ..models.flip_chips import FlipChip

# Create your views here.

class FlipChipListView(LoginRequiredMixin, ListView):
    context_object_name = "flip_chips"
    model = FlipChip
    template_name = 'engineering/flip_chips/flip_chip_list.html'

class FlipChipDetailView(LoginRequiredMixin, DetailView):
    model = FlipChip
    
    
class FlipChipCreateView(LoginRequiredMixin, CreateView):
    fields = ("serial_num", "bond_date", "created_by", "notes")
    model = FlipChip
    #form = forms.CreateProductForm()
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(FlipChipCreateView, self).form_valid(form)
    
    
class FlipChipUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("serial_num", "bond_date", "notes")
    model = FlipChip
    
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.serial_num)