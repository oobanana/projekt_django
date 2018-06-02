from django import forms
from .models import*

class SignUpForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'password']

