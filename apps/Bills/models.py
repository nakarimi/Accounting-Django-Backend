from django.db import models
from djmoney.models.fields import MoneyField
from ..bill_items.models import Bill_item
from ..Vendors.models import Vendor
# Create your models here.


class Bill(models.Model):
    class Meta:
        db_table = 'bill'

    def __str__(self):
        return "Bill Details"

    items = models.ForeignKey(Bill_item, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    total = MoneyField(max_digits=14, decimal_places=2,
                         default_currency='USD')
    balance = MoneyField(max_digits=14, decimal_places=2,
                        default_currency='USD')
    desc = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
