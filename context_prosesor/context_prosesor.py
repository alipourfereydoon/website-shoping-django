from  blog.models import article

def recent_article(request):
    recent_article=article.objects.order_by('created')
    return {'recent_article':recent_article}