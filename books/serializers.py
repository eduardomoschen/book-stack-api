from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer para o model Book.

    Atributos:
        Nenhum atributo específico nesta classe.

    Métodos:
        Nenhum método específica nesta classe.

    Campos:
        Todos os campos do model Book.
    """

    class Meta:
        model = Book
        fields = '__all__'
