from .models import Invoice, Invoice_num
from rest_framework import serializers


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceNumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_num
        fields = '__all__'
