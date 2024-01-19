from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para o model User.

    Atributos:
        - Esta classe não possui atributos.

    Métodos:
        - create: Cria um novo usuário com base nos dados validados.

    Campos:
        - id: Primary Key do usuário.
        - first_name: Primeiro nome do usuário.
        - last_name: Último nome do usuário
        - username: Nome de usuário escolhido pelo usuário.
        - email: E-mail do usuário.
        - phone_number: Número de telefone do usuário.
        - birth_date: Data de nascimento do usuário.
        - is_active: Indica se a conta do usuário está ativa.
        - is_staff: Indica se o usuário tem privilégios de staff.
        - is_superuser: Indica se o usuário tem privilégios de superuser.
    """

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'birth_date',
            'is_active',
            'is_staff',
            'is_superuser',
        )

    def create(self, validated_data):
        """
        Cria um novo usuário com base nos dados validados.

        Parâmetros:
            - validated_data: Dados validados para criação do usuário.

        Retorna:
            - User: Instância do usuário criado.
        """

        password = validated_data.pop('password', None)
        user = User(**validated_data)

        if password:
            user.password = make_password(password)

        user.save()
        return user
