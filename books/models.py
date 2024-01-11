from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class YearField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        current_year = datetime.date.today().year
        kwargs['validators'] = [
            MinValueValidator(1500),
            MaxValueValidator(current_year)
        ]
        kwargs['help_text'] = "Digite um ano (YYYY)"
        super().__init__(*args, **kwargs)

class Book(models.Model):
    isbn = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    year_of_publication = YearField()
    publisher = models.CharField(max_length=255, blank=True, null=True)
    image = models.URLField()
    available = models.BooleanField(default=True)
    waiting_list = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title
