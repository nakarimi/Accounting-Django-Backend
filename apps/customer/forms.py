from .models import Customer
from django.forms import ModelForm


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['label', 'owner', 'phone',
                  'status', 'email'
                #   , 'updated_at'
                  ]
