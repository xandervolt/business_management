#from django.http import JsonResponse
#from django.db import transaction
#from django.db import IntegrityError
#from django.template.loader import render_to_string
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

'''
def gwd_create(request):

    data = dict()
    with transaction.atomic():
        if request.method == 'POST':
            form = GaasWaferDesignForm(request.POST)
            if form.is_valid():
                form.instance.created_by = request.user
                form.save()
                data['form_is_valid'] = True
                gaas_wafer_designs = GaasWaferDesign.objects.all()
                redirect('engineering:gaas_wafer_design_list')
            else:
                data['form_is_valid'] = False
        else:
            form = GaasWaferDesignForm()

        context = {'form': form}
        data['html_form'] = render_to_string('engineering/gaas_wafer_designs/gaas_wafer_design_form_inner.html',
            context,
            request=request
        )
        return JsonResponse(data)
'''
'''
class TestFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form_inner.html'
    ajax_template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form_inner.html'
    form_class = GaasWaferDesignForm
    success_url = reverse_lazy('engineering:gaas_wafer_design_list')
    success_message = "Way to go!"
'''

class GaasWaferDesignCreateView(LoginRequiredMixin, CreateView):
    fields = ("design_ui", "emitting", "contact_location", "optical_power", "design_date", "designer", "design_document", "designer_ui", "in_trash", "inactive_date", "notes")
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form_inner.html'

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'engineering/gaas_wafer_designs/create_success.html', {'gaas_wafer_designs': self.object})

'''
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(GaasWaferDesignCreateView, self).form_valid(form)
'''

class GaasWaferDesignUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("design_ui", "emitting", "contact_location", "optical_power", "design_date", "designer", "design_document", "designer_ui", "in_trash", "inactive_date", "notes")
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form.html'

    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.design_ui)
