from django import forms
from django.core.exceptions import ValidationError

from outflows import models


class OutflowForm(forms.ModelForm):
    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(),
            'description': forms.Textarea(),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def __init__(self, *args, **kwargs):
        super(OutflowForm, self).__init__(*args, **kwargs)
        self.fields['product'].initial = ''
        self.fields['quantity'].initial = ''
        self.fields['description'].initial = ''

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} é de {product.quantity} unidades.'
            )

        return quantity
