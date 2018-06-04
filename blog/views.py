from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
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
        author=User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404

    try:
        posts=Post.objects.filter(autor=author).order_by('data')
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/blog.html',{'posts':posts, 'author':author})

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
    return render(request, 'blog/month_post.html',{'posts':posts, 'username':username, 'year':year, 'month':month})
def user(request,username):
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'blog/user.html',{'userr':user})
def post(request,id):
    try:
        post=Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404

    try:
        comments=Komentarz.objects.filter(post=post)
    except Komentarz.DoesNotExist:
        raise Http404
    return render(request, 'blog/post.html',{'post':post, 'comments':comments})

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
def addPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.autor = request.user
            post.data = timezone.now()
            post.save()
            return render(request, 'blog/post.html',{'post':post})
    else:
        form = PostForm
    return render(request, 'blog/editPostCom.html', {'form': form, 'header': "Dodaj post."})

def editPost(request,id):
    post = get_object_or_404(Post, pk = id)
    if post.autor != request.user:
        return HttpResponse("Błąd! Nie możesz edytować artykułów innych użytkowników.")
    try:
        comments=Komentarz.objects.filter(post=post)
    except Komentarz.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.autor = request.user
            post.save()
            return render(request, 'blog/post.html',{'post':post, 'comments':comments})
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/editPostCom.html', {'form': form, 'header': "Edytuj post."})

def deletePost(request, id):
    post = get_object_or_404(Post, pk = id)
    if post.autor != request.user:
        return HttpResponse("Błąd! Nie możesz usuwać artykułów innych użytkowników.")

    post.delete()
    return redirect('blogPage' , username = request.user.username)
def comment(request,id):
    post=get_object_or_404(Post, pk = id)
    try:
        comments=Komentarz.objects.filter(post=post)
    except Komentarz.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.autor = request.user
            comment.data = timezone.now()
            comment.post=post
            comment.save()
            return render(request, 'blog/post.html',{'post':post, 'comments':comments})
    else:
        form = CommentForm
    return render(request, 'blog/editPostCom.html', {'form': form, 'header': "Dodaj komentarz."})


