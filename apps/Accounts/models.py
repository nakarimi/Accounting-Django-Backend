from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.

class Account(models.Model):
    def __str__(self):
        return self.label

    label = models.CharField(max_length=20,unique=True)
    owner = models.CharField(max_length=20)
    balance = MoneyField(max_digits=14, decimal_places=2, 
                          default_currency='USD')
    desc = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

class Type(models.Model):
    label = models.CharField(max_length=20, unique=True)
