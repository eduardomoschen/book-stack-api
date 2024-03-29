from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    """

    """

    def _create_user(
        self,
        username,
        email,
        password,
        is_staff,
        is_superuser,
        **extra_fields
    ):
        now = timezone.now()
        if not username:
            raise ValueError(('The given username must be set.'))
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        """

        """

        return self._create_user(
            username,
            email,
            password,
            False,
            False,
            ' ',
            **extra_fields
        )

    def create_superuser(self, username, email, password, **extra_fields):
        """

        """

        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model personalizado de usuário para aplicação.

    Atributos:
        - first_name: Primeiro nome do usuário.
        - last_name: Sobrenome do usuário.
        - username: Nome de usuário único.
        - email: Endereço de e-mail único.
        - birth_date: Data de nascimento do usuário.
        - phone_number: Número de telefone do usuário.
        - is_active: Indica se a conta do usuário está ativa.
        - is_staff: Indica se o usuário tem privilégios de staff.
        - is_superuser: Indica se o usuário tem privilégios de superusuário.
        - date_joined: Data e hora de registro do usuário.

    Métodos:
        - __str__: Retorna o nome de usuário como representação em string.

    Atributos Especiais:
        - USERNAME_FIELD: Campo usado para autenticação (username).
        - REQUIRED_FIELDS: Campos adicionais necessários durante a criação.

    Gerenciador:
        - objects: Instância do UserManager para lidar com operações no banco
        de dados.
    """

    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
