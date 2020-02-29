from django.db import models

# Create your models here.


class Vendor(models.Model):
    class Meta:
        db_table = 'vendor'

    def __str__(self):
        return self.label

    label = models.CharField(max_length=50, null=True)
    desc=models.CharField(max_length = 200, blank = True)
    status=models.BooleanField(default = 1)
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)
