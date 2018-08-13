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
from reportlab.pdfgen import canvas

from ..models.purchase_orders import PurchaseOrder, PurchaseOrderItem
from ..forms import PurchaseOrderForm, PurchaseOrderItemForm

# Create your views here.

class PurchaseOrderListView(LoginRequiredMixin, ListView):
    context_object_name = "purchase_orders"
    model = PurchaseOrder
    template_name = 'financial/purchase_orders/purchase_order_list.html'


class PurchaseOrderDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'financial/purchase_orders/purchase_order_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PurchaseOrderDetailView, self).get_context_data(**kwargs)
        context['purchase_order'] = PurchaseOrder.objects.get(pk=self.kwargs['pk'])
        context['items'] = PurchaseOrderItem.objects.filter(po_number_fk=self.kwargs['pk'])
        return context


class PurchaseOrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'financial/purchase_orders/purchase_order_form.html'
    #ajax_template_name = 'financial/purchase_orders/purchase_order_form_inner.html'
    form_class = PurchaseOrderForm
    form = PurchaseOrderForm()
    model = PurchaseOrder
    #success_url = reverse_lazy('financial:purchase_order_list')
    #success_message = "GaAs Wafer Design Created Successfully!"

    def form_valid(self, form):
        '''
        object = form.save(commit=False) #prevent save of form
        object.created_by = self.request.user #set created_by to request user

        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

        # Create the PDF object, using the response object as its "file."
        object.po_document = canvas.Canvas(response)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        object.po_document.drawString(100, 100, "Hello world.")

        # Close the PDF object
        object.po_document.showPage()
        #object.po_document.save()

        # now save the object/form
        object.save()
        '''
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()

        return super(PurchaseOrderCreateView, self).form_valid(form)


class PurchaseOrderItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'financial/purchase_orders/purchase_order_item_form.html'
    form_class = PurchaseOrderItemForm
    success_url = '/'
    form = PurchaseOrderForm()
    model = PurchaseOrder
    '''
    def get_context_data(self, **kwargs):
        context = super(PurchaseOrderItemCreateView, self).get_context_data(**kwargs)
        context['purchase_order'] = PurchaseOrder.objects.get(pk=self.kwargs['pk'])
        context['items'] = PurchaseOrderItem.objects.filter(po_number_fk=self.kwargs['pk'])
        return context
    '''
    def form_valid(self, form):
        '''
        object = form.save(commit=False) #prevent save of form
        object.created_by = self.request.user #set created_by to request user

        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

        # Create the PDF object, using the response object as its "file."
        object.po_document = canvas.Canvas(response)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        object.po_document.drawString(100, 100, "Hello world.")

        # Close the PDF object
        object.po_document.showPage()
        #object.po_document.save()

        # now save the object/form
        object.save()
        '''
        object = form.save(commit=False)
        #object.created_by = self.request.user
        object.save()


'''
class PurchaseOrderUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("design_ui", "emitting", "contact_location", "optical_power", "design_date", "designer", "design_document", "designer_ui", "in_trash", "inactive_date", "notes")
    model = GaasWaferDesign
    template_name = 'engineering/gaas_wafer_designs/gaas_wafer_design_form.html'

    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.design_ui)
'''
