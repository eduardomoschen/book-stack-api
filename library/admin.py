from django.contrib import admin
from .models import BookBorrowing, Notification

@admin.register(BookBorrowing)
class BookBorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'date_issued', 'due_date', 'returned')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if change:  # Atualização de BookBorrowing
            original_obj = BookBorrowing.objects.get(pk=obj.pk)
            original_returned = original_obj.returned
            new_returned = obj.returned

            if original_returned and not new_returned:  # Verifica se o livro está sendo marcado como não devolvido
                book = obj.book
                book.available = False  # Define o livro como indisponível ao ser emprestado
                book.save()
        else:
            book = obj.book
            book.available = False
            book.save()

        super().save_model(request, obj, form, change)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    ...
