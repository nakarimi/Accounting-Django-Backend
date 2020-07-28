from .models import Member
from rest_framework import serializers


class MemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = Member
    fields = ['id', 'first_name', 'email', 'last_name', 'phone',
                'posistion', 'created_at', 'updated_at']
