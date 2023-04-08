from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega campos adicionales para el perfil de usuario aquí
    imagen_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    telefono = models.CharField(max_length=10)
    hobbies = models.CharField(max_length=100)
    formacion=models.CharField(max_length=100)
    redes_sociales=models.CharField(max_length=100)
    # Otros campos de perfil de usuario aquí

    def __str__(self):
        return self.user.username
