from django.db import models

class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)

    def __str__(self):
        return self.username


