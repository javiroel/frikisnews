from django import forms
from django.forms import ModelForm, Textarea 
from .models import tusnoticias, Contact
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CrearNoticia(forms.ModelForm):

      class Meta:
        model = tusnoticias
        fields = ['id','titulo','subtitulo','noticia_text','pub_date','image']

        widgets = {

        'titulo': forms.TextInput(attrs={'class':'form-control'}),  

        'subtitulo': forms.TextInput(attrs={'class':'form-control'}),

       'noticia_text': forms.Textarea(attrs={'class': 'form-control'}),

       'image': forms.ClearableFileInput(attrs={'multiple': True}),

        }

        image= forms.ImageField()

        lebels = {
                   
          'titulo': 'Titulo', 
          'subtitulo': 'Subtitulo',
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
        fields = ['titulo','subtitulo','noticia_text','image']

        widgets = {

        'titulo': forms.TextInput(attrs={'class':'form-control'}),  
        
        'subtitulo': forms.TextInput(attrs={'class':'form-control'}),

       'noticia_text': forms.Textarea(attrs={'class': 'form-control'}),

        }

        lebels = {
                   
          'titulo': 'Titulo', 
          'subtitulo': 'Subtitulo',
          'noticia_text' : 'Noticia',
        

        }  


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

