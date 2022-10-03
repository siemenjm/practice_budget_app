from django.db import models

class Institution(models.Model):
    institution_id = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    logo = models.URLField(max_length=500, default='https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Dollar_Sign.svg/500px-Dollar_Sign.svg.png?20120706173622')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['institution_id']

class Account(models.Model):
    account_id = models.CharField(max_length=250)
    balance_available = models.IntegerField(default=0)
    balance_current = models.IntegerField(default=0)
    name = models.CharField(max_length=250)
    account_type = models.CharField(max_length=250)
    account_subtype = models.CharField(max_length=250)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='accounts')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['account_id']
