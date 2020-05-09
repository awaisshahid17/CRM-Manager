from django import forms
from .models import Promocode
from crm_manager.models import Promocode
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password


class PromocodeForm(forms.ModelForm):

    code = forms.CharField(required=True,
                           error_messages={'required': 'Enter Code'},
                           widget=forms.TextInput
                           (attrs={'class': 'form-control', 'placeholder': 'Code'})
                           )
    amount_percent = forms.CharField(required=True,
                                     error_messages={'required': 'This field is required'},
                                     widget=forms.TextInput
                                     (attrs={'class': 'form-control', 'placeholder': 'amount_percent'})
                                     )

    class Meta:
        model = Promocode
        fields = ["code", 'type', 'amount_percent', 'is_free', 'is_Available']

    widgets = {
        'code': forms.TextInput(attrs={'class': 'form-control'}),
        'amount_percent': forms.TextInput(attrs={'class': 'form-control'}),
    }
