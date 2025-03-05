from django.db import models

class article(models.Model):
    title=models.CharField(max_length=50)
    body= models.TextField()
    image=models.ImageField(upload_to='images/articles')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

