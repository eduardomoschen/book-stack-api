from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import BookBorrowing
from .serializers import BookBorrowingSerializer
from .permissions import (
    LibraryPermissionClass,
    LibraryUserOwnerOrAdminPermissionClass
)


class BookBorrowingCreateListView(generics.ListCreateAPIView):
    permission_classes = (LibraryPermissionClass,)
    queryset = BookBorrowing.objects.all()
    serializer_class = BookBorrowingSerializer


class BookBorrowingDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (LibraryUserOwnerOrAdminPermissionClass,)
    queryset = BookBorrowing.objects.all()
    serializer_class = BookBorrowingSerializer
    lookup_field = 'id'
