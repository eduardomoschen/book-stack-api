from django.contrib import admin
from .models import BookBorrowing, Notification

@admin.register(BookBorrowing)
class BookBorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'date_issued', 'due_date', 'returned')

    def save_model(self, request, obj, form, change):
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
    ...
