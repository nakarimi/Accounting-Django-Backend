# Generated by Django 2.2.7 on 2020-07-08 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_auto_20200522_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
    ]
