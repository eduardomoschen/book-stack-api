from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .permissions import (
    UserAdminPermissionClass,
    UserOwnerOrAdminPermissionClass
)

class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    View para listar e realizar a criação de contas dos usuários.

    Atributos:
        - permission_classes: Lista de classes de permissão a serem vericadas.
        - queryset: Conjunto de dados a ser utilizado pela view.
        - serializer_class: Classe serializadora a ser utilizada para converter
        os dados.

    Métodos:
        - Não há métodos nesta classe.
    """

    permission_classes = (UserAdminPermissionClass,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para visualizar, atualizar e excluir detalhes de um empréstimo
    específico. Além disso, também é possível realizar a devolução do livro.

    Atributos:
        - permission_class: Lista de classes de permissão a serem verificadas.
        - queryset: Conjunto de dados a ser utilizado pela view.
        - serializer_class: Classe serializadora a ser utilizada para converter
        os dados.
        - lookup_field: Campo utilizado para identificar o user na URL.

    Métodos:
        - Não há métodos nesta classe.
    """

    permission_classes = (UserOwnerOrAdminPermissionClass,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
