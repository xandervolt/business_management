from django.http import JsonResponse
#from django.db import transaction
#from django.db import IntegrityError
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    FormView,
)

from ..models.gaas_wafer_designs import GaasWaferDesign
from ..forms import GaasWaferDesignForm
from .. mixins import AjaxTemplateMixin

# Create your views here.

class GaasWaferDesignListView(LoginRequiredMixin, ListView):
    context_object_name = "gaas_wafer_designs"
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_list.html'


class GaasWaferDesignDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "gaas_wafer_design"
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_detail.html'


def gaas_create(request):
    form = GaasWaferDesignForm()
    context = {'form': form}
    html_form =  render_to_string('engineering/gaas_wafer_designs/gaas_wafer_design_form_inner.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form': html_form})


class GaasWaferDesignFormView(SuccessMessageMixin, AjaxTemplateMixin, CreateView):
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form.html'
    ajax_template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form_inner.html'
    form_class = GaasWaferDesignForm
    model = GaasWaferDesign
    form = GaasWaferDesignForm()
    success_url = reverse_lazy('engineering:gaas_wafer_design_list')
    success_message = "Way to go!"


class GaasWaferDesignCreateView(LoginRequiredMixin, CreateView):
    fields = ("design_ui", "emitting", "contact_location", "optical_power", "design_date", "designer", "design_document", "designer_ui", "in_trash", "inactive_date", "notes")
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form_inner.html'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(GaasWaferDesignCreateView, self).form_valid(form)


class GaasWaferDesignUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("design_ui", "emitting", "contact_location", "optical_power", "design_date", "designer", "design_document", "designer_ui", "in_trash", "inactive_date", "notes")
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form.html'

    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.design_ui)
