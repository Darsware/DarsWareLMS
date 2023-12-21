from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# Create index view function
def index(request):
    return HttpResponse("Hello, world. You're at the courses index.")
