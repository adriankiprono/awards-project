from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    awards = Award.objects.all()
    
    return render(request,'home.html',{"awards":awards})

def search_results(request):
    
    if 'website' in request.GET and request.GET["website"]:
        search_term = request.GET.get("website")
        searched_website = Award.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-website/search.html',{"message":message,"websites": searched_websites})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-website/search.html',{"message":message})
