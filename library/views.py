from rest_framework import generics
from .models import BookBorrowing
from .serializers import BookBorrowingSerializer
from .permissions import (
    LibraryPermissionClass,
    LibraryUserOwnerOrAdminPermissionClass
)


class BookBorrowingCreateListView(generics.ListCreateAPIView):
    """
    View para listar e realizar o empréstimo de livros.

    Atributos:
        - permission_classes: Lista de classes de permissão a serem vericadas.
        - queryset: Conjunto de dados a ser utilizado pela view.
        - serializer_class: Classe serializadora a ser utilizada para converter
        os dados.

    Métodos:
        - Não há métodos nesta classe.
    """

    permission_classes = (LibraryPermissionClass,)
    queryset = BookBorrowing.objects.all()
    serializer_class = BookBorrowingSerializer


class BookBorrowingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para visualizar, atualizar e excluir detalhes de um empréstimo
    específico. Além disso, também é possível realizar a devolução do livro.

    Atributos:
        - permission_class: Lista de classes de permissão a serem verificadas.
        - queryset: Conjunto de dados a ser utilizado pela view.
        - serializer_class: Classe serializadora a ser utilizada para converter
        os dados.
        - lookup_field: Campo utilizado para identificar o emrpréstimo na URL.

    Métodos:
        - Não há métodos nesta classe.
    """

    permission_classes = (LibraryUserOwnerOrAdminPermissionClass,)
    queryset = BookBorrowing.objects.all()
    serializer_class = BookBorrowingSerializer
    lookup_field = 'id'
