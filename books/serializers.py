from rest_framework import serializers
from .models import Book
import requests
from io import BytesIO
from django.core.files.base import ContentFile

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

  
