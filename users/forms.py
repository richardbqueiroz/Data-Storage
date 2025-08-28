from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

from users.models import User


class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username', 'full_name', 'email', 'cpf', 'birth_date', 'phone_number',
            'is_active', 'is_staff', 'is_superuser'
        ]
        widgets = {
            'username': forms.TextInput(),
            'full_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'cpf': forms.TextInput(),
            'birth_date': forms.DateInput(),
            'phone_number': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
            'is_staff': forms.CheckboxInput(),
            'is_superuser': forms.CheckboxInput(),
        }
        labels = {
            'username': 'Nome de Usuário',
            'full_name': 'Nome Completo',
            'email': 'Email',
            'cpf': 'CPF',
            'birth_date': 'Data de Nascimento',
            'phone_number': 'Número de Telefone',
            'is_active': 'Ativo',
            'is_staff': 'Administrador',
            'is_superuser': 'Superusuário',
        }

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = ''
        self.fields['full_name'].initial = ''
        self.fields['email'].initial = ''
        self.fields['cpf'].initial = ''
        self.fields['phone_number'].initial = ''
        self.fields['password1'].initial = ''
        self.fields['password2'].initial = ''

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.instance and self.instance.username == username:
            return username
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username', 'full_name', 'email', 'cpf', 'birth_date', 'phone_number',
            'is_active', 'is_staff', 'is_superuser'
        ]
        widgets = {
            'username': forms.TextInput(),
            'full_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'cpf': forms.TextInput(),
            'birth_date': forms.DateInput(),
            'phone_number': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
            'is_staff': forms.CheckboxInput(),
            'is_superuser': forms.CheckboxInput(),
        }
        labels = {
            'username': 'Nome de Usuário',
            'full_name': 'Nome Completo',
            'email': 'Email',
            'cpf': 'CPF',
            'birth_date': 'Data de Nascimento',
            'phone_number': 'Número de Telefone',
            'is_active': 'Ativo',
            'is_staff': 'Administrador',
            'is_superuser': 'Superusuário',
        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = ''
        self.fields['full_name'].initial = ''
        self.fields['email'].initial = ''
        self.fields['cpf'].initial = ''
        self.fields['phone_number'].initial = ''

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.instance and self.instance.username == username:
            return username
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())
