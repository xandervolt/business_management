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
        toggle = UserActivity.objects.current(request.user)
        users_data = UserActivity.objects.filter(user=request.user).order_by('-timestamp')
        current_users = UserActivity.objects.order_by('user', '-timestamp').distinct('user')
        context = {}
        context['toggle'] = toggle
        context['users_data'] = users_data
        context['current_users'] = current_users
        return render(request, "administration/timesheets/user-activity.html", context)

    def post(self, request, *args, **kwargs):
        context = {}
        toggle = UserActivity.objects.toggle(request.user)
        users_data = UserActivity.objects.filter(user=request.user).order_by('-timestamp')
        current_users = UserActivity.objects.order_by('user', '-timestamp').distinct('user')
        context['toggle'] = toggle
        context['users_data'] = users_data
        context['current_users'] = current_users
        return render(request, "administration/timesheets/user-activity.html", context)

class CheckinUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("status")
    model = UserActivity
    template_name = 'administration/timesheets/checkin_update_form.html'


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

'''
