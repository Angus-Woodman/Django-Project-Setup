from django.shortcuts import render

from .models import Dog

# Create your views here.
from django.http import HttpResponse

def index(req):
    dogs = Dog.objects.all()
    dogNames = ''
    for dog in dogs:
        dogNames += f' {dog.name} ,'
    return HttpResponse(f'<h1>Hello! Here are all the friends who need adopting!<h1> <p>{dogNames}</p>')

def about(req):
    return HttpResponse("<h1>This is an animal adomption django setup example<h1>")

def show(req, id):
    dog = Dog.objects.get(pk=id)
    print(dog)
    return HttpResponse(f'<h3>Meet {dog.name}!</h3>')
