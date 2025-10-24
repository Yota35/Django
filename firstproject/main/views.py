from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1> Web development with Ike <h1>")

def v1(response):
    return HttpResponse("<h1> View 1 <h1>")