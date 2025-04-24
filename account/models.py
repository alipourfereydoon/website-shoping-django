from django.contrib.auth.models import User
from django.db import models

# class user(models.Model):
#     username=models.CharField(max_length=50)
#     email=models.CharField(max_length=50)
#     password1=models.CharField(max_length=50)
#     password2=models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.username


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fathers_name=models.CharField(max_length=50)
    melicode=models.CharField(max_length=20)
    image=models.ImageField(upload_to='profiles/images',blank=True,null=True)

    def __str__(self):
        return self.user.username