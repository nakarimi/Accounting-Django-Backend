from django.db import models
from ..customer.models import Customer

# Create your models here.
class Invoice(models.Model):
    class Meta:
        db_table = 'invoice'

    def __str__(self):
        return self.inv_number

    inv_number = models.CharField(max_length=20, default=0, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    currency = models.CharField(max_length=5)
    total_price = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    due_date = models.DateField()
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Invoice_num(models.Model):
    class Meta:
        db_table = 'invoice_num'
    
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
