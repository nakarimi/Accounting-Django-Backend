from django.db import models
from django.forms import ModelForm

# Create your models here.


class Company(models.Model):
    def __str__(self):
        return "Company Details"

    com_name = models.CharField(max_length=20, verbose_name ='Company Name')
    com_email = models.CharField(max_length=20, verbose_name ="Email")
    com_website = models.CharField(max_length=20, verbose_name ="Website", null=True )
    com_owner = models.CharField(max_length=20, verbose_name ="Owner")
    com_status = models.BooleanField(verbose_name ="Status")
    com_address = models.CharField(max_length=20, verbose_name ="Address")
    com_phone = models.CharField(max_length=10, verbose_name ="Phone")
    com_logo = models.FileField(upload_to='companies/', verbose_name ="Logo", null=True)
    pub_date = models.DateTimeField( auto_now_add=True)


