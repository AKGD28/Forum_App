from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # Importer settings pour accéder à AUTH_USER_MODEL
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Remplacer 'auth.User' par 'settings.AUTH_USER_MODEL'
    # Autres champs

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Remplacer 'auth.User' par 'settings.AUTH_USER_MODEL'
    # Autres champs

class CustomUser(AbstractUser):
    # Ajout d'un champ 'bio' ou d'autres champs personnalisés si nécessaire
    bio = models.TextField(max_length=500, blank=True, null=True)
    
    # Tu peux aussi ajouter d'autres champs si tu en as besoin
    def __str__(self):
        return self.username  

# 
