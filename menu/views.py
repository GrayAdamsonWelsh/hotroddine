from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_menu(request):
    return HttpResponse("Hello, This is the menus!")