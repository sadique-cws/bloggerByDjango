from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *

def home(r):
    data = {
        "category":Category.objects.all(),
        "posts" : Post.objects.all()
    }
    return render(r, "home.html",data)

def viewNews(r,slug):
    data = {
        "category":Category.objects.all(),
        "post" : Post.objects.get(slug=slug),
        "related_posts" :Post.objects.exclude(slug=slug)
    }
    return render(r,"view.html",data)

@login_required()
def insertNews(r):
    form = PostForm(r.POST or None, r.FILES or None)
    data = {
        "form":form,
        "category":Category.objects.all()
    }

    if r.method == "POST":
        formData = form.save(commit=False)
        formData.author = r.user
        formData.save()
        return redirect(home)
    
    return render(r, "insert.html",data)

def deleteNews(r,slug):
    data = Post.objects.get(slug=slug)
    data.delete()
    return redirect(home)

def editNews(r,slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(r.POST or None, r.FILES or None, instance=post)
    data = {
        "form":form,
        "category":Category.objects.all()
    }

    if r.method == "POST":
        formData = form.save(commit=False)
        formData.author = r.user
        formData.save()
        return redirect(home)
    
    return render(r, "insert.html",data)

def signUp(r):
    form = UserCreationForm(r.POST or None)
    data = {
        "form":form
    }
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(signIn)
    return render(r,"accounts/register.html",data) 

def signIn(r):
    form = AuthenticationForm(r.POST or None)
    data = {
        "form":form
    }

    if r.method == "POST":
        username = r.POST.get("username")
        password = r.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(r,user)
            return redirect(home)
    return render(r,"accounts/login.html",data)

def filterCategory(r,id):
    data = {
        "posts":Post.objects.filter(category__id=id),
        "category":Category.objects.all()
    }
    return render(r, "home.html",data)

def searchNews(r):
    search = r.GET.get('search')
    data = {
        "posts":Post.objects.filter(title__icontains=search),
        "category":Category.objects.all()
    }
    return render(r, "home.html",data) 

def signOut(r):
    logout(r)
    return redirect(home)