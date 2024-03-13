from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_signup(request):
    return HttpResponse("Hello, sign up!")