from django.db import models
from ..Bills.models import Bill
from ..Invoices.models import Invoice
from djmoney.models.fields import MoneyField
from ..Accounts.models import Account

# Create your models here.


class Payment(models.Model):
    class Meta:
        db_table = 'payment'

    def __str__(self):
        return self.label

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    label = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20)
    pay_type = models.CharField(max_length=20)
    ref_bill = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=True)
    ref_inv = models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=True)
    amount = MoneyField(max_digits=14, decimal_places=2,
                         default_currency='USD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
