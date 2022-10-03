from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Account, Institution

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class InstitutionList(TemplateView):
    template_name = 'institution_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get('name')
        if name != None:
            context['institutions'] = Institution.objects.filter(name__icontains=name)
            context['header'] = f'Searching for {name}'
        else:
            context["institutions"] = Institution.objects.all()
            context['header'] = 'Your Institutions'

        return context

class InstitutionCreate(CreateView):
    model = Institution
    fields = ['institution_id', 'name', 'logo']
    template_name = 'institution_create.html'
    success_url = '/institutions/'

class InstitutionDetail(DetailView):
    model = Institution
    template_name = 'institution_detail.html'

class AccountList(TemplateView):
    template_name = 'account_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["accounts"] = Account.objects.all()
        context['header'] = 'Your Accounts'

        # name = self.request.GET.get('name')
        # if name != None:
        #     context['institutions'] = Institution.objects.filter(name__icontains=name)
        #     context['header'] = f'Searching for {name}'
        # else:
        #     context["institutions"] = Institution.objects.all()
        #     context['header'] = 'Your Institutions'

        return context

class AccountCreate(CreateView):
    model = Account
    fields = ['account_id', 'balance_available', 'balance_current', 'name', 'account_type', 'account_subtype', 'institution']
    template_name = 'account_create.html'
    success_url = '/accounts/'
