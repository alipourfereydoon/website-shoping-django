from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


def user_login(request):
    if request.user.is_authenticated==True:
        return redirect('home_app:main')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user =authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home_app:main')
    return render(request ,'account/login.html',context={})

def user_register(request):
    context={'eroors':[]}
    if request.user.is_authenticated==True:
        return  redirect('home_app:main')
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 != password2:
            context['eroors'].append('this tow password is not the same')
        return render(request,'account/register.html',context)

        user=User.objects.create(first_name=username,last_name=email,email=password1)
        login(request, user)
        return redirect('home_app:main')
    return render(request,'account/register.html',context={})


def user_logout(request):
    logout(request)
    return  redirect('home_app:main')
