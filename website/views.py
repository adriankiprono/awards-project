from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    awards = Award.objects.all()
    
    return render(request,'home.html',{"awards":awards})

def search_results(request):
    
    if 'award' in request.GET and request.GET["award"]:
        search_term = request.GET.get("award")
        searched_awards = Award.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-website/search.html',{"message":message,"awards": searched_awards})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-website/search.html',{"message":message})
