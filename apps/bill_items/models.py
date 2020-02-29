from django.db import models
from ..entity.models import Entity
# Create your models here.


class Bill_item(models.Model):
    class Meta:
        db_table = 'bill_item'
    def __str__(self):
        return self.label

    label = models.CharField(max_length=50, null=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
