from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Account, Institution, Transaction, Tag
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

@method_decorator(login_required, name='dispatch')
class InstitutionList(TemplateView):
    template_name = 'institution_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get('name')
        if name != None:
            context['institutions'] = Institution.objects.filter(name__icontains=name, user = self.request.user)
            context['header'] = f'Searching for {name}'
        else:
            context["institutions"] = Institution.objects.filter(user = self.request.user)
            context['header'] = 'Your Institutions'

        return context

@method_decorator(login_required, name='dispatch')
class InstitutionCreate(CreateView):
    model = Institution
    fields = ['institution_identification', 'name', 'logo']
    template_name = 'institution_create.html'
    success_url = '/institutions/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InstitutionCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class InstitutionDetail(DetailView):
    model = Institution
    template_name = 'institution_detail.html'

@method_decorator(login_required, name='dispatch')
class InstitutionUpdate(UpdateView):
    model = Institution
    fields = ['institution_id', 'name', 'logo']
    template_name = 'institution_update.html'

    def get_success_url(self):
        return reverse('institution_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class InstitutionDelete(DeleteView):
    model = Institution
    template_name = 'institution_delete_confirmation.html'
    success_url = '/institutions/'

@method_decorator(login_required, name='dispatch')
class AccountList(TemplateView):
    template_name = 'account_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["accounts"] = Account.objects.filter(user=self.request.user)
        context['header'] = 'Your Accounts'

        return context

@method_decorator(login_required, name='dispatch')
class AccountCreate(CreateView):
    model = Account
    fields = ['account_identification', 'balance_available', 'balance_current', 'name', 'account_type', 'account_subtype', 'institution']
    template_name = 'account_create.html'
    success_url = '/accounts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AccountCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class AccountDetail(DetailView):
    model = Account
    template_name = 'account_detail.html'

@method_decorator(login_required, name='dispatch')
class AccountUpdate(UpdateView):
    model = Account
    fields = ['account_id', 'balance_available', 'balance_current', 'name', 'account_type', 'account_subtype', 'institution']
    template_name = 'account_update.html'

    def get_success_url(self):
        return reverse('account_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class AccountDelete(DeleteView):
    model = Account
    template_name = 'account_delete_confirmation.html'
    success_url = '/accounts/'

@method_decorator(login_required, name='dispatch')
class TransactionList(TemplateView):
    template_name = 'transaction_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["transactions"] = Transaction.objects.filter(user = self.request.user)
        context['header'] = 'Your Transactions'

        return context

@method_decorator(login_required, name='dispatch')
class TransactionCreate(CreateView):
    model = Transaction
    fields = ['amount', 'description', 'category', 'sub_category', 'sub_sub_category', 'debited_account', 'credited_account', 'transaction_date']
    template_name = 'transaction_create.html'
    success_url = '/transactions/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TransactionCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class TransactionDetail(DetailView):
    model = Transaction
    template_name = 'transaction_detail.html'

@method_decorator(login_required, name='dispatch')
class TransactionUpdate(UpdateView):
    model = Transaction
    fields = ['amount', 'description', 'category', 'sub_category', 'sub_sub_category', 'debited_account', 'credited_account', 'transaction_date']
    template_name = 'transaction_update.html'

    def get_success_url(self):
        return reverse('transaction_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class TransactionDelete(DeleteView):
    model = Transaction
    template_name = 'transaction_delete_confirmation.html'
    success_url = '/transactions/'

@method_decorator(login_required, name='dispatch')
class TagList(TemplateView):
    template_name = 'tag_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tags"] = Tag.objects.filter(user = self.request.user)
        context['header'] = 'Your Tags'

        return context

@method_decorator(login_required, name='dispatch')
class TagCreate(CreateView):
    model = Tag
    fields = ['title']
    template_name = 'tag_create.html'
    success_url = '/tags/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TagCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class TagDetail(DetailView):
    model = Tag
    template_name = 'tag_detail.html'

@method_decorator(login_required, name='dispatch')
class TagTransactionAssoc(View):
    def get(self, request, pk, transaction_pk):
        assoc = request.GET.get('assoc')
        if assoc == 'remove':
            Tag.objects.get(pk=pk).transactions.remove(transaction_pk)
        if assoc == 'add':
            Tag.objects.get(pk=pk).transactions.add(transaction_pk)
        
        return redirect('/tags/')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account_list')
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)