from rest_framework import serializers

from .models import BookBorrowing


class BookBorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookBorrowing
        fields = '__all__'

    def create(self, validated_data):
        book_borrowing = BookBorrowing.objects.create(**validated_data)
        book = book_borrowing.book

        book.available = False
        book.save()

        return book_borrowing

    def update(self, instance, validated_data):
        returned_borrowing = super().update(instance, validated_data)
        book = returned_borrowing.book

        book.available = True
        book.save()

        return returned_borrowing
