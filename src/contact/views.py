from django.conf import settings
from django.contrib import  messages
from django.shortcuts import render

# from .models import Contact
# Create your views here.

def home(request):
    return render(request,"index.html")
