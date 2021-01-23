from django.shortcuts import render
from rest_framework import viewsets
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer

class Author_view(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
class Book_view(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
