from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import BookBorrowing
from books.models import Book

User = get_user_model()


class BookBorrowingSerializer(serializers.ModelSerializer):
    """
    Serializer para o model BookBorrowing.

    Atributos:
        - book: Campo de primary key relacionado ao model Book.

    Métodos:
        - validate_book: Valida se o livro está disponível e, caso contrário,
        adiciona o usuário à lista de espera.
        - create: Cria um novo empréstimo de livro e marca o livro como não
        disponível.
        - update: Atualiza o empréstimo do livro e marca o livro como
        disponível se devolvido e atualiza a lista de espera.

    Campos:
        - Todos os campos do model Book.

    Nota:
        - O campo 'book' é read-only para eivtar que seja alterado durante a
        criação ou atualização.
    """

    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = BookBorrowing
        fields = '__all__'
        read_only_fields = ('book',)

    def validate_book(self, value):
        """
        Valida se o livro está disponível e, caso contrário, adiciona o usuário
        à lista de espera.

        Caso o livro não esteja disponível, uma exceção será levantada
        informando que o usuário foi adicionado à lista de espera.
        """

        try:
            book = Book.objects.get(id=value.id)
            if not book.available:
                users = self.initial_data.get('borrower', [])
                if not isinstance(users, list):
                    users = [users]

                for user_id in users:
                    user = User.objects.get(id=user_id)
                    if user not in book.waiting_list.all():
                        book.waiting_list.add(
                            user,
                            through_defaults={'time_added': timezone.now()}
                        )
                book.save()
                raise serializers.ValidationError(
                    'This book is not currently available. You have been added \
to the waiting list.'
                )

            return book
        except Book.DoesNotExist:
            raise serializers.ValidationError('Book does not exist.')


    def create(self, validated_data):
        """
        Cria um novo empréstimo de livro e marca o livro como não disponível.
        """

        book = validated_data.get('book')

        if not book.available:
            raise serializers.ValidationError(
                'This book is not currently available.'
            )

        book_borrowing = BookBorrowing.objects.create(**validated_data)

        book.available = False
        book.save()

        return book_borrowing

    def update(self, instance, validated_data):
        """
        Atualiza o empréstimo do livro e marca o livro como disponível quando
        for devolvido e atualiza a lista de espera.
        """

        returned_borrowing = super().update(instance, validated_data)
        book = returned_borrowing.book

        if returned_borrowing.returned and book.waiting_list.exists():
            user = book.waiting_list.all().first()
            book.waiting_list.remove(user)

        book.available = True
        book.save()

        return returned_borrowing
