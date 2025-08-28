from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('full_name', 'email', 'cpf', 'phone_number', 'birth_date')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'cpf', 'phone_number', 'birth_date', 'is_active', 'is_staff', 'is_superuser')


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User

    list_display = ('username', 'full_name', 'email', 'cpf', 'phone_number', 'birth_date', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'full_name', 'email', 'cpf', 'phone_number', 'birth_date', 'password')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Datas', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'email', 'cpf', 'phone_number', 'birth_date', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'cpf', 'full_name')
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
