from django.db import models
from ..Products.models import Product
# Create your models here.


class Item(models.Model):
    def __str__(self):
        return self.label

    label = models.CharField(max_length=50, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
