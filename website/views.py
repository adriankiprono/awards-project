from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    awards = Award.objects.all()
    
    return render(request,'home.html',{"awards":awards})
