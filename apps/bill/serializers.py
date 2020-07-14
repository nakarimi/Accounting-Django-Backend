from .models import Bill, Bill_num
from rest_framework import serializers


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class BillNumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill_num
        fields = '__all__'
