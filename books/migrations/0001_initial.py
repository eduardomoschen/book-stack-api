# Generated by Django 5.0 on 2023-12-28 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('year_of_publication', models.DateField()),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
