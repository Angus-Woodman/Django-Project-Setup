from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(req):
    return HttpResponse("<h1>Hello! Here are all the friends who need adopting!<h1>")

def about(req):
    return HttpResponse("<h1>This is an animal adomption django setup example<h1>")

def show(req, id):
    return HttpResponse(f'<h3>Dog number {id}!</h3>')
