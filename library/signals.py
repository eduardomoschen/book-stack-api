from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from dotenv import load_dotenv
import os
from .models import BookBorrowing, Notification

load_dotenv()


@receiver(post_save, sender=BookBorrowing)
def send_return_notification(sender, instance, created, **kwargs):
    if created:
        one_day_before = instance.due_date - timedelta(days=1)
        if one_day_before == timezone.now().date():
            borrower = instance.borrower
            book_title = instance.book.title

            Notification.objects.create(
                user=borrower,
                message=f'You have a book ({book_title}) with 1-day return.'
            )

            user_email = borrower.email
            username = borrower.username

            send_mail(
                f'Return Alert: Book "{book_title}" Return in 1 Day',
                f'Hello, {username}.\n\n'
                f'This is a gentle reminder that the deadline for returning the\
 book "{book_title}" is approaching. There is only 1 day left until the \
stipulated return date.',
                os.getenv('DEFAULT_FROM_EMAIL'),
                [user_email],
                fail_silently=False
            )

@receiver(post_save, sender=BookBorrowing)
def send_delay_notification(sender, instance, **kwargs):
    if instance.returned is False and instance.due_date < timezone.now().date():
        borrower = instance.borrower
        book_title = instance.book.title
        days_delayed = (timezone.now().date() - instance.due_date).days

        user_email = borrower.email
        username = borrower.username

        Notification.objects.create(
            user=borrower,
            message=f'You have an overdue book ({book_title}).'
        )

        send_mail(
            f'Delay Alert: Book "{book_title}" Return Overdue',
            f'Hello, {username}.\n\n'
            f'This is a notification that the book "{book_title}" is \
{days_delayed} days overdue. '
            f'Please return the book as soon as possible to avoid further \
penalties.',
            os.getenv('DEFAULT_FROM_EMAIL'),
            [user_email],
            fail_silently=False
        )

@receiver(post_save, sender=BookBorrowing)
def notify_waiting_list(sender, instance, **kwargs):
    if instance.returned and instance.book.waiting_list.exists():
        book = instance.book
        user = book.waiting_list.first()
        book.waiting_list.remove(user)

        book.available = True
        book.save()

        book_title = book.title
        user_email = user.email
        username = user.username

        Notification.objects.create(
            user=user,
            message=f'The book ({book_title}) is now available.'
        )

        send_mail(
            f'Book "{book_title}" is now available',
            f'Hello, {username}.\n\n'
            f'The book "{book_title}" that you were waiting for is now \
available.'
            f'You can borrow it from the library.',
            os.getenv('DEFAULT_FROM_EMAIL'),
            [user_email],
            fail_silently=False
        )
