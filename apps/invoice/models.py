from django.db import models
from ..item.models import Item
from ..customer.models import Customer

# Create your models here.
class Invoice(models.Model):
    class Meta:
        db_table = 'invoice'

    def __str__(self):
        return self.inv_number

    inv_number = models.CharField(max_length=20)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    currency = models.CharField(max_length=5)
    total_price = models.IntegerField()
    balance = models.IntegerField()
    due_date = models.DateField()
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)