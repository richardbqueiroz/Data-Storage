from django import forms

from products import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price']
        widgets = {
            'title': forms.TextInput(),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(),
            'serie_number': forms.TextInput(),
            'cost_price': forms.NumberInput(),
            'selling_price': forms.NumberInput(),
        }
        labels = {
            'title': 'Título',
            'category': 'Categoria',
            'brand': 'Marca',
            'description': 'Descrição',
            'serie_number': 'Número de Série',
            'cost_price': 'Preço de Custo',
            'selling_price': 'Preço de Venda',
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['title'].initial = ''
        self.fields['category'].initial = ''
        self.fields['brand'].initial = ''
        self.fields['description'].initial = ''
        self.fields['serie_number'].initial = ''
        self.fields['cost_price'].initial = ''
        self.fields['selling_price'].initial = ''
