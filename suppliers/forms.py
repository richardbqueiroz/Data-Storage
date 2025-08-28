from django import forms

from suppliers import models


class SupplierForm(forms.ModelForm):

    class Meta:
        model = models.Supplier
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        self.fields['name'].initial = ''
        self.fields['description'].initial = ''
