from django import forms

from inflows import models


class InflowForm(forms.ModelForm):

    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(),
            'description': forms.Textarea(),
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def __init__(self, *args, **kwargs):
        super(InflowForm, self).__init__(*args, **kwargs)
        self.fields['supplier'].initial = ''
        self.fields['product'].initial = ''
        self.fields['quantity'].initial = ''
        self.fields['description'].initial = ''
