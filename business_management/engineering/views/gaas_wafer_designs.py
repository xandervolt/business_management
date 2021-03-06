from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
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
import json
from django.contrib import messages

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


class GaasWaferDesignCreateView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin, CreateView):
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form.html'
    ajax_template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form_inner.html'
    form_class = GaasWaferDesignForm
    form = GaasWaferDesignForm()
    model = GaasWaferDesign
    success_url = reverse_lazy('engineering:gaas_wafer_design_list')
    success_message = "GaAs Wafer Design Created Successfully!"

    def form_valid(self, form):
        """
        If the request is ajax, save the form and return a json response.
        Otherwise return super as expected.
        """
        if self.request.is_ajax():
            self.object = form.save(commit=False)
            self.object.created_by = self.request.user
            self.object = form.save()
            return HttpResponse(json.dumps("success"),
                content_type="application/json")

        else:
            object = form.save(commit=False)
            object.created_by = self.request.user
            object.save()

        return super(GaasWaferDesignCreateView, self).form_valid(form)

    def form_invalid(self, form):
        """
        We haz errors in the form. If ajax, return them as json.
        Otherwise, proceed as normal.
        """
        if self.request.is_ajax():
            return HttpResponseBadRequest(json.dumps(form.errors),
                content_type="application/json")
        return super(GaasWaferDesignCreateView, self).form_invalid(form)


class GaasWaferDesignUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("design_ui", "emitting", "contact_location", "optical_power", "design_date", "designer", "design_document", "designer_ui", "in_trash", "inactive_date", "notes")
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form.html'

    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.design_ui)
