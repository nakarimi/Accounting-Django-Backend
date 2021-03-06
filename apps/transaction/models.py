from django.db import models
from ..account.models import Account
from ..payment.models import Payment
# Create your models here.


class Transaction(models.Model):
    class Meta:
        db_table = 'transaction'

    def __str__(self):
        return self.label

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.IntegerField()
    currency = models.CharField(max_length=5,default='USD')
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
