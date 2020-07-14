from django.db import models
from ..bill.models import Bill
from ..invoice.models import Invoice
from ..account.models import Account

# Create your models here.


class Payment(models.Model):
    class Meta:
        db_table = 'payment'

    def __str__(self):
        return self.label

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    currency = models.CharField(max_length=5, default='USD')
    ref_bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True)
    ref_inv = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
