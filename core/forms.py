from django import forms
from core.models import beneficiary, marital_status, cities, status

class beneficiaryModelForm(forms.ModelForm):
    class Meta:
        model = beneficiary
        fields = [
            'name',
            'cpf',
            'id_doc',
            'issuing_authority',
            'issuing_date',
            'marital_status',
            'profession',
            'cep_address',
            'street',
            'address',
            'number_address',
            'city',
            'main_phone',
            'other_phone',
            'email',
            'status_person',
            'date_of_birth',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'id_doc': forms.TextInput(attrs={'class': 'form-control'}),
            'issuing_authority': forms.TextInput(attrs={'class': 'form-control'}),
            'issuing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'cep_address': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'number_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'main_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'other_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'status_person': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }