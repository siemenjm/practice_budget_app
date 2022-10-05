from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Account, Institution, Transaction
from django.urls import reverse

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

class InstitutionUpdate(UpdateView):
    model = Institution
    fields = ['institution_id', 'name', 'logo']
    template_name = 'institution_update.html'

    def get_success_url(self):
        return reverse('institution_detail', kwargs={'pk': self.object.pk})

class AccountList(TemplateView):
    template_name = 'account_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["accounts"] = Account.objects.all()
        context['header'] = 'Your Accounts'

        return context

class AccountCreate(CreateView):
    model = Account
    fields = ['account_id', 'balance_available', 'balance_current', 'name', 'account_type', 'account_subtype', 'institution']
    template_name = 'account_create.html'
    success_url = '/accounts/'

class AccountDetail(DetailView):
    model = Account
    template_name = 'account_detail.html'

class AccountUpdate(UpdateView):
    model = Account
    fields = ['account_id', 'balance_available', 'balance_current', 'name', 'account_type', 'account_subtype', 'institution']
    template_name = 'account_update.html'

    def get_success_url(self):
        return reverse('account_detail', kwargs={'pk': self.object.pk})

class AccountDelete(DeleteView):
    model = Account
    template_name = 'account_delete_confirmation.html'
    success_url = '/accounts/'

class TransactionList(TemplateView):
    template_name = 'transaction_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["transactions"] = Transaction.objects.all()
        context['header'] = 'Your Transactions'

        return context

class TransactionCreate(CreateView):
    model = Transaction
    fields = ['amount', 'description', 'category', 'sub_category', 'sub_sub_category', 'debited_account', 'credited_account', 'transaction_date']
    template_name = 'transaction_create.html'
    success_url = '/transactions/'

class TransactionDetail(DetailView):
    model = Transaction
    template_name = 'transaction_detail.html'

class TransactionUpdate(UpdateView):
    model = Transaction
    fields = ['amount', 'description', 'category', 'sub_category', 'sub_sub_category', 'debited_account', 'credited_account', 'transaction_date']
    template_name = 'transaction_update.html'

    def get_success_url(self):
        return reverse('transaction_detail', kwargs={'pk': self.object.pk})

class TransactionDelete(DeleteView):
    model = Transaction
    template_name = 'transaction_delete_confirmation.html'
    success_url = '/transactions/'
