# Generated by Django 2.2.7 on 2020-08-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='total',
            field=models.CharField(max_length=20),
        ),
    ]