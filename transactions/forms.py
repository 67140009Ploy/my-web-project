from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'transaction_type', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control-custom'}),
            'transaction_type': forms.Select(choices=Transaction.TYPE_CHOICES, attrs={'class': 'form-control-custom'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control-custom'}),
        }
