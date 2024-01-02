from rest_framework import generics
from .models import BookBorrowing
from .serializers import BookBorrowingSerializer


class BookBorrowingCreateListView(generics.ListCreateAPIView):
    queryset = BookBorrowing.objects.all()
    serializer_class = BookBorrowingSerializer


class BookBorrowingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookBorrowing.objects.all()
    serializer_class = BookBorrowingSerializer
    lookup_field = 'id'
