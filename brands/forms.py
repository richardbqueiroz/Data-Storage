from django import forms

from brands import models


class BrandForm(forms.ModelForm):

    class Meta:
        model = models.Brand
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
        super(BrandForm, self).__init__(*args, **kwargs)
        self.fields['name'].initial = ''
        self.fields['description'].initial = ''
