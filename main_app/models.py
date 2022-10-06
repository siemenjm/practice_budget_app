from datetime import date
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    institution_identification = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    logo = models.URLField(max_length=500, default='https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Dollar_Sign.svg/500px-Dollar_Sign.svg.png?20120706173622')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Account(models.Model):
    account_identification = models.CharField(max_length=250)
    balance_available = models.IntegerField(default=0)
    balance_current = models.IntegerField(default=0)
    name = models.CharField(max_length=250)
    account_type = models.CharField(max_length=250)
    account_subtype = models.CharField(max_length=250)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='accounts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    sub_category = models.CharField(max_length=250, default='')
    sub_sub_category = models.CharField(max_length=250, default='')
    debited_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='debit_transactions', blank=True, null=True)
    credited_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credit_transactions', blank=True, null=True)
    transaction_date = models.DateField(default=date.today)
    transaction_identification = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['description']

class Tag(models.Model):
    title = models.CharField(max_length=250)
    transactions = models.ManyToManyField(Transaction, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
