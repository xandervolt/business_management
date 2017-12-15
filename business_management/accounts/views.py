from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView
from allauth.account.views import ConfirmEmailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User


class ConfirmEmailView(ConfirmEmailView):
    pass

class AccessDeniedView(TemplateView):
    template_name = 'account/access_denied.html'