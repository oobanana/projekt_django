from django.db import models
from django.contrib.auth.models import *

# Create your models here.
# class Uzytkownik(models.Model):
#     imie=models.CharField(max_length=20)
#     nazwisko=models.CharField(max_length=20)
#     email=models.CharField(max_length=50)
#     login=models.CharField(max_length=20)
#     haslo=models.CharField(max_length=20)
class Post(models.Model):
    tytul=models.CharField(max_length=50)
    tresc=models.TextField(max_length=1000, null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    data=models.DateTimeField('data opublikowania')
    haslo=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.tytul + " - " +self.autor.username
class Komentarz(models.Model):
    tresc=models.TextField(max_length=100,null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    data=models.DateTimeField('data opublikowania')
    post=models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
class Odpowiedz_komentarz(models.Model):
    komentarz=models.ForeignKey(Komentarz, on_delete=models.CASCADE)
    odpowiedz=models.ForeignKey(Komentarz, on_delete=models.CASCADE,related_name="odpowiedz")

