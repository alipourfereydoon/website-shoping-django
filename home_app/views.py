from django.shortcuts import render
from blog.models import article

def home(request):
    articles=article.objects.all()
    return render(request,"home_app/index.html",context={'articles':articles})
