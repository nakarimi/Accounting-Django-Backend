from .models import Bill_item
from rest_framework import serializers


class Bill_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill_item
        fields = '__all__'
