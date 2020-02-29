from django.db import models
from djmoney.models.fields import MoneyField
from ..Accounts.models import Account
from ..Payments.models import Payment
# Create your models here.


class Transaction(models.Model):
    class Meta:
        db_table = 'transaction'

    def __str__(self):
        return self.label

    label = models.CharField(max_length=20, unique=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=14, decimal_places=2,
                         default_currency='USD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
