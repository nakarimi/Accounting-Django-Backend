from .models import Company
from django.forms import ModelForm


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['com_name', 'com_email',
                  'com_owner', 'com_status', 'com_address',
                  'com_phone']
