from .models import Invoice
from rest_framework import serializers


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id',
          'inv_number',
          'items',
          'customer',
          'currency',
          'total_price',
          'balance',
          'due_date',
          'status',
          'created_at',
          'updated_at']
