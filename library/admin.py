from django.contrib import admin
from .models import BookBorrowing, Notification

@admin.register(BookBorrowing)
class BookBorrowingAdmin(admin.ModelAdmin):
    """
    Admin para o model BookBorrowing.

    Lista todos os empréstimos de livros com informações relevantes, incluindo
    o livro, o usuário que fez o empréstimo, a data do empréstimo, a data
    esperada para a devolução e se foi devolvido.

    Métodos:
        - save_model: Sobrescreve o método para atualizar o status de
        disponibilidade do livro quando um empréstimo é salvo no admin.
    """

    list_display = ('book', 'borrower', 'date_issued', 'due_date', 'returned')

    def save_model(self, request, obj, form, change):
        """
        Atualiza o status de disponibilidade do livro quando um empréstimo é
        realizado.

        Se o empréstimo for alterado e marcado como devolvido, o livro é
        marcado como disponível. Se um novo empréstimo for adicionado, o livro
        é marcado como não disponível.

        Parâmetros:
            - request: Objeto HttpRequest recebido durante a solicitação.
            - obj: Instância do model BookBorrowing sendo salva.
            - form: Formulário utilizado para editar o model BookBorrowing.
            - change: Indica se é uma atualização de um empréstimo existente.
        """

        super().save_model(request, obj, form, change)

        if change:
            original_obj = BookBorrowing.objects.get(pk=obj.pk)
            original_returned = original_obj.returned
            new_returned = obj.returned

            if original_returned and not new_returned:
                book = obj.book
                book.available = False
                book.save()
        else:
            book = obj.book
            book.available = False
            book.save()

        super().save_model(request, obj, form, change)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Admin para o model Notification.

    Métodos:
        Não há métodos nesta classe.
    """

    ...
