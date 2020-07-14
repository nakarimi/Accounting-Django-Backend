from django.db import models
from ..vendor.models import Vendor

# Create your models here.
class Bill(models.Model):
    class Meta:
        db_table = 'bill'

    def __str__(self):
        return self.bill_number

    bill_number = models.CharField(max_length=20, default=0, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    currency = models.CharField(max_length=5)
    total_price = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    due_date = models.DateField()
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bill_num(models.Model):
    class Meta:
        db_table = 'bill_num'
    
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
