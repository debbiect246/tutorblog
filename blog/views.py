from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
    #this function links to urls.py in blog directory so view knows where to go for url

def about(request):
    return HttpResponse('<h1>Blog About</h1>')