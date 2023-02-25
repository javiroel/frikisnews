import datetime

from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,User


# Create your models here.
class tusnoticias(models.Model):
    titulo=models.CharField(max_length=30)
    noticia_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.noticia_text} - {str(self.pub_date)}-{str(self.titulo)}"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class frikisuser(models.Model):
    name = models.CharField(max_length=30)
    nick= models.CharField(max_length=10)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {str(self.nick)} {str(self.age)}"

class frikisseccion(models.Model):
    namegroup = models.CharField(max_length=30)
    seccionname= models.CharField(max_length=10)

    def __str__(self):
        return f"{self.namegroup} - {str(self.seccionname)}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name    


       