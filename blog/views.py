from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')
    #this function links to home page in templates folder in blog app.

def about(request):
    return render(request, 'blog/about.html')
    #this function links to blog page in templates folder in blog app.