# Generated by Django 2.2.7 on 2020-05-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.BooleanField(default=1),
        ),
        migrations.DeleteModel(
            name='Inv_num',
        ),
    ]
