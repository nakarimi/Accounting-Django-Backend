from .models import Member
from django.forms import ModelForm


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone',
                  'posistion', 'email'
                #   , 'updated_at'
                  ]
