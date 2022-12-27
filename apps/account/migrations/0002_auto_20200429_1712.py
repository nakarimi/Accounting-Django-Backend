# Generated by Django 2.2.7 on 2020-04-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='balance_currency',
        ),
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='account',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(),
        ),
    ]