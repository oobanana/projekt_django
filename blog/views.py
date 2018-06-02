from django.shortcuts import render
from .models import *
from django.http import Http404

# Create your views here.

def homePage(request):
    return render(request, 'blog/home.html',{})
def blog(request, username):
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404

    try:
        posts=Post.objects.filter(autor=user).order_by('data')
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/blog.html',{'posts':posts, 'username':username})

def year_post(request,username,year):
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404

    try:
        posts=Post.objects.filter(autor=user,data__year=year).order_by('data')
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/year_post.html',{'posts':posts, 'username':username, 'year':year})
def month_post(request,username,year,month):
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404

    try:
        posts=Post.objects.filter(autor=user,data__year=year,data__month=month).order_by('data')
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/year_post.html',{'posts':posts, 'username':username, 'year':year, 'month':month})
def user(request,username):
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'blog/user.html',{'user':user})
def post(request,id):
    try:
        post=Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/post.html',{'post':post})
