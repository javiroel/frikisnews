from django import forms
from django.forms import ModelForm, Textarea 
from .models import tusnoticias
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CrearNoticia(forms.ModelForm):

      class Meta:
        model = tusnoticias
        fields = ['id','titulo','noticia_text','pub_date']

        widgets = {

        'titulo': forms.TextInput(attrs={'class':'form-control'}),  

       'noticia_text': forms.Textarea(attrs={'class': 'form-control'}),

        }

        lebels = {
                   
          'titulo': 'Titulo', 
          'noticia_text' : 'Noticia',
        

        }  
class FormularioLogin(AuthenticationForm):
    pass

class FormularioRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditaNoticia(forms.ModelForm):

      class Meta:
        model = tusnoticias
        fields = ['titulo','noticia_text']

        widgets = {

        'titulo': forms.TextInput(attrs={'class':'form-control'}),  

       'noticia_text': forms.Textarea(attrs={'class': 'form-control'}),

        }

        lebels = {
                   
          'titulo': 'Titulo', 
          'noticia_text' : 'Noticia',
        

        }  