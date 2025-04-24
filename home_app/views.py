from django.shortcuts import render,redirect
from blog.models import article
from django.urls import reverse

def home(request):
    articles=article.objects.all()
    recent_articles=article.objects.all()[:3]
    return render(request,"home_app/index.html",context={'articles':articles,'recent_articles':recent_articles})
