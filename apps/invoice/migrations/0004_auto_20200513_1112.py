# Generated by Django 2.2.7 on 2020-05-13 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_invoice_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='inv_number',
            field=models.CharField(default=0, max_length=20),
        ),
    ]