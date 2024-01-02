# Generated by Django 5.0 on 2023-12-29 01:05

import books.models
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_of_publication',
            field=books.models.YearField(help_text='Digite um ano (YYYY)', validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)]),
        ),
    ]