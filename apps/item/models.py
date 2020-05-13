from django.db import models
from ..invoice.models import Invoice

# Create your models here.
class Item(models.Model):
    class Meta:
        db_table = 'item'

    def __str__(self):
        return self.label

    label = models.CharField(max_length=50, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
