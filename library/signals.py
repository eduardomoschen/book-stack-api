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
