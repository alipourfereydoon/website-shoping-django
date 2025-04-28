from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class category(models.Model):
    title=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return  self.title

class article(models.Model):
    CHOICE=(
        ('A','PYTHON'),
        ('B','DJANGO')
    )
    author=models.ForeignKey(User,on_delete=models.SET_DEFAULT,default='1')
    title=models.CharField(max_length=50,choices=CHOICE,unique_for_date='pub_date')
    category=models.ManyToManyField(category)
    body= models.TextField()
    image=models.ImageField(upload_to='images/articles')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    pub_date=models.DateField(default=timezone.now())
    myfile=models.FileField(upload_to='test',null=True)
    slug=models.SlugField(null=True,unique=True)

    class Meta:
        ordering=('-created',)


    def get_absolute_url(self):
        return reverse("blog:article-detail" , kwargs={'slug':self.slug})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

class Comment(models.Model):
    article=models.ForeignKey(article,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')

    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.body[:50]








