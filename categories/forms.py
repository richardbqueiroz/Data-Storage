from django import forms

from categories import models


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
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
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].initial = ''
        self.fields['description'].initial = ''
