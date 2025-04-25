from django.shortcuts import render,get_object_or_404
from blog.models import article
from django.core.paginator import Paginator


def post_detail(request,title):
    ads=get_object_or_404(article,slug=slug)
    return render(request, "blog/post-details.html",context={'article':ads})


def article_list(request):
    articles=article.objects.all()
    page_number=request.GET.get('page')
    paginator=Paginator(articles,1)
    object_list=paginator.get_page(page_number)
    return render(request ,'blog/article_list.html',context={'articles':object_list})


