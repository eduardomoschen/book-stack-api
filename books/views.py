from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permissions import BookPermissionClass

class BookListCreateView(generics.ListCreateAPIView):
    permission_classes = (BookPermissionClass,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, BookPermissionClass)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'
