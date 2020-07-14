from .models import Vendor
from rest_framework import serializers


class VendorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vendor
    fields = ['id', 'label', 'email', 'owner', 'phone', 'desc',
                'status', 'created_at', 'updated_at']
