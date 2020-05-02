from django.db import models

class File(models.Model):
    label = models.CharField(max_length=50, null=True)
    owner = models.CharField(max_length=20)
    balance = models.IntegerField(default=1)
    currency = models.CharField(max_length=5, blank=True)
    desc = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name


