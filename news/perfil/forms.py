from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('imagen_perfil', 'telefono','hobbies','formacion', 'redes_sociales')

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('imagen_perfil', 'telefono','hobbies','formacion', 'redes_sociales')