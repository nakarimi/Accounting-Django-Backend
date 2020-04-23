from .models import Vendor
from django.forms import ModelForm


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['label', 'owner', 'phone',
                  'status', 'email', 'desc'
                #   , 'updated_at'
                  ]
