from django.db import models

# Create your models here.


class Member(models.Model):
    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.first_name

    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, unique=True)
    posistion = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
