from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import *


# Create your views here.

def index(request):
    socials = Social.objects.all().order_by("-id")[:10]
    socials_random = Social.objects.all().order_by("?")[:4]
    context = {
        "socials" : socials,
        "socials_random" : socials_random,
    }
    return render(request,'index.html', context)

def detail(request,id):
    social = Social.objects.get(id=id)
    socials_random = Social.objects.all().order_by("?")[:4]
    comments = Comment.objects.filter(social = social)
    
    if request.method == "POST":
        name1 = request.POST["name"]
        comment1 = request.POST["comment"]
        comm = Comment(name = name1, comment = comment1, social = social)
        comm.save()
        return HttpResponseRedirect('/detail/'+id + "/") 
        
    
    context = {
        "social" : social,
        "socials_random" : socials_random,
        "comments" : comments,
    }
    return render(request, 'detail.html',context)


def explore(request,id='all'):
    socials_random = Social.objects.all().order_by("?")[:4]
    if id.isnumeric():
        socials = Social.objects.filter( category = id ).order_by("-id")
    else:
        socials = Social.objects.all().order_by("-id") 
         
    categorys = Category.objects.all()
    
    
    #paginator
    paginator = Paginator(socials, 3) 
    page_number = request.GET.get('page')
    socials = paginator.get_page(page_number)
    context = {
        "socials" : socials,
        "socials_random" : socials_random,
        "categorys" : categorys,
        }
    return render(request, 'explore.html',context)  




   