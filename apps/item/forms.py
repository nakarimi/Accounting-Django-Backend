from .models import Account
from django.forms import ModelForm


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['label', 'owner', 'balance',
                  'desc', 'status', 'currency'
                #   , 'updated_at'
                  ]
