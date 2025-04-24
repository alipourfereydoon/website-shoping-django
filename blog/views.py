from django.shortcuts import render,get_object_or_404
from blog.models import article

def post_detail(request,title):
    ads=get_object_or_404(article,slug=slug)
    return render(request, "blog/post-details.html",context={'article':ads})


def article_list(request):
    articles=article.objects.all()
    return render(request ,'blog/article_list.html',context={'articles':articles})


