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
)
import json

from ..models.contacts import Contact
from ..forms import ContactForm
from ..mixins import AjaxTemplateMixin


class ContactListCreateView(LoginRequiredMixin, CreateView, ListView):
    context_object_name = "contacts"
    model = Contact
    template_name = 'administration/contacts/contact_list_create.html'
    #ajax_template_name = 'administration/contacts/contacts_list_create.html'
    form_class = ContactForm
    form = ContactForm()
    success_url = reverse_lazy('administration:contact_list')

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

        return super(ContactListCreateView, self).form_valid(form)

    def form_invalid(self, form):
        """
        We haz errors in the form. If ajax, return them as json.
        Otherwise, proceed as normal.
        """
        if self.request.is_ajax():
            return HttpResponseBadRequest(json.dumps(form.errors),
                content_type="application/json")
        return super(ContactListCreateView, self).form_invalid(form)


class ContactListView(LoginRequiredMixin, ListView):
    context_object_name = "contacts"
    model = Contact
    template_name = 'administration/contacts/contact_list.html'


class ContactCreateView(LoginRequiredMixin, CreateView):
    context_object_name = "contacts"
    model = Contact
    template_name = 'administration/contacts/contact_form.html'
    form_class = ContactForm
    form = ContactForm()
    success_url = reverse_lazy('administration:contact_list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(ContactCreateView, self).form_valid(form)


class ContactDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "contacts"
    model = Contact
    template_name = 'administration/contacts/contact_detail.html'
