from django.contrib import admin
from .models import Account, Institution, Transaction, Tag

admin.site.register(Account)
admin.site.register(Institution)
admin.site.register(Transaction)
admin.site.register(Tag)