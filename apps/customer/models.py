from django.db import models

# Create your models here.


class Customer(models.Model):
    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.label

    label = models.CharField(max_length=50, null=True)
    owner = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
