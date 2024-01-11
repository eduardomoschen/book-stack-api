from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permissions import BookPermissionClass

class BookListCreateView(generics.ListCreateAPIView):
    """
    View para listar e criar livros.

    Atributos:
        - permission_class: Lista de classes de permissão a serem verificadas.
        - queryset: Conjunto de dados a ser utilizado pela view.
        - serializer_class: Classe serializadora a ser utilizada para converter
        os dados.
    """

    permission_classes = (BookPermissionClass,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para visualizar, atualizar e excluir detalhes de um livro específico.

    Atributos:
        - permission_class: Lista de classes de permissão a serem verificadas.
        - queryset: Conjunto de dados a ser utilizado pela view.
        - serializer_class: Classe serializadora a ser utilizada para converter
        os dados.
        - lookup_field: Campo utilizado para identificar o livro na URL.
    """

    permission_classes = (IsAuthenticated, BookPermissionClass)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'
