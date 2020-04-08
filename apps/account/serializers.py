from .models import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'label', 'owner', 'balance',
          'desc', 'status', 'created_at', 'updated_at']
