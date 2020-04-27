from django.db import models

# Create your models here.
class Item(models.Model):
    class Meta:
        db_table = 'item'

    def __str__(self):
        return self.label

    label = models.CharField(max_length=50, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
