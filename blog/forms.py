from django import forms
from .models import*


class SignUpForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'password']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['tytul', 'tresc']
class CommentForm(forms.ModelForm):
    class Meta:
        model=Komentarz
        fields=['tresc']
