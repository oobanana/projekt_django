from django.shortcuts import render
from .models import *
from django.http import Http404
from django.views.generic import View
from .forms import *
from django.contrib.auth import authenticate, login

# Create your views here.

def homePage(request):
    return render(request, 'blog/home.html',{})
def blog(request, username):
    try:
        users=User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404

    try:
        posts=Post.objects.filter(autor=users).order_by('data')
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/blog.html',{'posts':posts, 'users':users})

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

class userRegister(View):
    def get(self, request):
        form = SignUpForm(None)
        return render(request, 'blog/register.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)

            return render(request, 'blog/user.html', {'okienko': "Zostałeś pomyślnie zarejestrowany."})

        else:
            return render(request, 'blog/register.html', {'form': form, 'okienko': "Błąd!!! Użytkownik już istnieje. Spróbuj ponownie."})
