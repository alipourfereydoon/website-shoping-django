from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class article(models.Model):
    CHOICE=(
        ('A','PYTHON'),
        ('B','DJANGO')
    )
    author=models.ForeignKey(User,on_delete=models.SET_DEFAULT,default='1')
    title=models.CharField(max_length=50,choices=CHOICE,unique_for_date='pub_date')
    body= models.TextField()
    image=models.ImageField(upload_to='images/articles')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    pub_date=models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

