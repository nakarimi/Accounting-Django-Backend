# Generated by Django 2.2.7 on 2020-05-13 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20200513_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice_num',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.Invoice')),
            ],
            options={
                'db_table': 'invoice_num',
            },
        ),
    ]