from django.shortcuts import render

from .models import Dog

# Create your views here.
from django.http import HttpResponse

def index(req):
    context = { 'doggos': Dog.objects.all() }
    return render(req, 'adoption/index.html', context)

def about(req):
    return render(req, 'adoption/about.html')

def show(req, id):
    dog = Dog.objects.get(pk=id)
    print(dog)
    return HttpResponse(f'<h3>Meet {dog.name}!</h3>')
