from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Book, Hero
from .serializers import BookSerializer, HeroSerializer


# Create your views here.
def index(request):
    return HttpResponse("ok")


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


