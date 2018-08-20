from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    FormView,
)

from django.utils import timezone

from ..models.timesheets import UserActivity


# Views here
class ActivityView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        context = {}
        toggle = UserActivity.objects.current(request.user)
        context['toggle'] = toggle
        return render(request, "administration/timesheets/user-activity.html", context)

    def post(self, request, *args, **kwargs):
        context = {}
        toggle = UserActivity.objects.toggle(request.user)
        context['toggle'] = toggle
        return render(request, "administration/timesheets/user-activity.html", context)


'''
class TimesheetListView(LoginRequiredMixin, CreateView, ListView):
    context_object_name = "timesheets"
    fields = ('week_start', )
    model = Timesheet
    template_name = 'administration/employees/timesheet_list.html'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.employee = self.request.user
        object.save()
        return super(TimesheetListView, self).form_valid(form)


class TimesheetDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "timesheet"
    model = Timesheet
    template_name = 'administration/employees/timesheet_detail.html'


class ClockPunchInView(LoginRequiredMixin, CreateView):
    context_object_name = "clock_punch"
    fields = ['punch_in_time', 'punched_in',]
    model = ClockPunch
    template_name = 'pages/layout.html'
    success_url = '/'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.employee = self.request.user
        object.punch_in_time = timezone.now()
        object.punched_in = True
        object.save()
        return super(ClockPunchInView, self).form_valid(form)


class ClockPunchOutView(LoginRequiredMixin, CreateView):
    context_object_name = "clock_punch"
    model = ClockPunch
    fields = ['punch_out_time', 'punched_out',]
    #form_class = PunchOutForm
    template_name = 'pages/layout.html'
    success_url = '/'

    def form_valid(self, form):
        object = form.save(commit=False)
        last_entry = ClockPunch.objects.filter(employee=self.request.user).order_by('-punch_in_time')[0]

        if last_entry.punch_in_time:
            object.employee = self.request.user
            object.punch_out_time = timezone.now()
            object.punched_out = True
            object.save()
            return super(ClockPunchOutView, self).form_valid(form)
        else:
            return redirect('/')


class ClockPunchDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "timesheet"
    model = Timesheet
    template_name = 'administration/employees/timesheet_detail.html'
'''
