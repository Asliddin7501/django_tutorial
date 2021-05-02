import json

from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from restapi_tutorial.models import Book, Author
from restapi_tutorial.serializers import BookSerializer, AuthorSerializer


class BookView(View):
    def get(self, request):
        book = Book.objects.get(id=2)
        serializer = BookSerializer(book)
        book_data_bytes = JSONRenderer().render(serializer.data)
        book_data_string = book_data_bytes.decode("utf-8")
        book_data_dict = json.loads(book_data_string)
        print(type(book_data_dict))
        return render(request, 'restapi_tutorial/book.html', {
            "book_data": book_data_dict
        })


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer