from django.db import models
from ..bill.models import Bill

# Create your models here.
class Bill_item(models.Model):
    class Meta:
        db_table = 'bill_item'

    def __str__(self):
        return self.label

    label = models.CharField(max_length=50, null=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.CharField(max_length=20)
    desc = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
