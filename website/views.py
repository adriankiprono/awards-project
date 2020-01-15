from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NewAwardForm


# Create your views here.
@login_required(login_url='/accounts/login/')
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
        message = "You haven't searched for any website"
        return render(request, 'all-website/search.html',{"message":message})
@login_required(login_url='/accounts/login/')
def website(request,website_id):
    try:
        website = Article.objects.get(id = website_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-website/website.html", {"website":website})
