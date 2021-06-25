from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>deneme sayfası bu içerik viewdan geldi</h1>")
