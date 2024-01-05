from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book


User = get_user_model()


class BookBorrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    date_issued = models.DateField()
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    date_delivered = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book} - {self.borrower}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.message}'
