from .models import Invoice
from django.forms import ModelForm


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = [
          'inv_number',
          'customer',
          'currency',
          'total_price',
          'balance',
          'due_date',
          'status',
        ]
