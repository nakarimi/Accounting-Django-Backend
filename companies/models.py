from django.db import models

# Create your models here.


class Company(models.Model):
    com_name = models.CharField(max_length=20, verbose_name ='Company Name')
    com_email = models.CharField(max_length=20, verbose_name ="Email")
    com_website = models.CharField(max_length=20, verbose_name ="Website")
    com_owner = models.CharField(max_length=20, verbose_name ="Owner")
    com_status = models.BooleanField(verbose_name ="Status")
    com_address = models.CharField(max_length=20, verbose_name ="Address")
    com_phone = models.CharField(max_length=10, verbose_name ="Phone")
    com_logo = models.FileField(upload_to='uploads/companies/', verbose_name ="Logo")
    pub_date = models.DateTimeField('date published')
