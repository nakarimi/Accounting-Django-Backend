from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.


class Entity(models.Model):
    class Meta:
        db_table = 'entity'

    def __str__(self):
        return self.label

    label = models.CharField(max_length=50, null=True)
    price = MoneyField(max_digits=10, decimal_places=2,
                       default_currency='USD')
    image = models.FileField(blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
