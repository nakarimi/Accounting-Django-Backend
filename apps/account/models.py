from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.


class Account(models.Model):
    class Meta:
        db_table = 'account'

    def __str__(self):
        return self.label

    label = models.CharField(max_length=20, unique=True)
    owner = models.CharField(max_length=20)
    balance = MoneyField(max_digits=14, decimal_places=2,
                         default_currency='USD', blank=True)
    desc = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
