from django.db import models
from ..Items.models import Item
from ..Customers.models import Customer
from djmoney.models.fields import MoneyField
# Create your models here.


class Invoice(models.Model):
    def __str__(self):
        return self.inv_number

    inv_number = models.CharField(max_length=20)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = MoneyField(max_digits=14, decimal_places=2,
                          default_currency='USD')
    due_date = models.DateField()
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
