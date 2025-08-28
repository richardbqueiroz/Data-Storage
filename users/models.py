from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None
    date_joined = None
    username = models.CharField(verbose_name="Nome de Usuário", max_length=255, unique=True)
    full_name = models.CharField(verbose_name="Nome Completo", max_length=255)
    email = models.EmailField(verbose_name="E-mail", max_length=255, unique=True)
    cpf = models.CharField(verbose_name="CPF", max_length=11, unique=True)
    phone_number = models.CharField(verbose_name="Contato", max_length=15, unique=True)
    birth_date = models.DateField(verbose_name="Data de Nascimento", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)
    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    is_staff = models.BooleanField(verbose_name="Administrador", default=False)
    is_superuser = models.BooleanField(verbose_name="Superusuário", default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'cpf']

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = 'users'

    def __str__(self):
        return f"{self.email} | {self.full_name} | {self.cpf}"
