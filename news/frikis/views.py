from pyexpat.errors import messages
from django.shortcuts import render, redirect,get_list_or_404,get_object_or_404
from .models import tusnoticias
from frikis.forms import CrearNoticia, EditaNoticia
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django import forms
from django.contrib import messages
from .forms import FormularioLogin
from .forms import FormularioRegistro,ContactForm
from django.contrib.auth import login, authenticate



# Create your views here.

from django.http import HttpResponse

def index(request):
    latest_news= tusnoticias.objects.all()
    context = {'latest_news': latest_news}
    return render(request, 'frikis/index.html', context)

 #def noticias(request, tusnoticias_id):
    #return HttpResponse("Estos son los resultados de las noticias %s."% tusnoticias_id )  

@login_required
def creanews(request):
     
    if request.method == "POST":
        form=CrearNoticia(request.POST,request.FILES)
        if form.is_valid():
          noticia=form.save() 
          noticia.autor=request.user  
          noticia.save()
          return redirect('creanews')

    else:
   
     form = CrearNoticia(initial={'pub_date':datetime.datetime.now() , 'autor':request.user})

    return render(request,'frikis/crearnoticia.html',{'form':form})


def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')
    else:
        form = FormularioRegistro()
    return render(request, 'frikis/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        # Procesar los datos del formulario de inicio de sesión
        form = FormularioLogin(request.POST)
        if form.is_valid():
            # Validar el usuario y contraseña
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # El usuario y contraseña son válidos, iniciar sesión
                login(request, user)
                return redirect('mi_vista')
            else:
                # El usuario y contraseña son inválidos, mostrar un mensaje de error
                messages.error(request, 'Usuario o contraseña inválidos')
    else:
        form = FormularioLogin()
    return render(request, 'frikis/login.html', {'form': form})    


@login_required

def edit(request, tusnoticias_id):

    noticia= tusnoticias.objects.filter(id=tusnoticias_id).first()

    formulario=EditaNoticia(instance=noticia)
  
    return render(request,'frikis/modificar.html',{'form': formulario, 'noticia':noticia})      


@login_required
def listar(request):
     noticias= tusnoticias.objects.all()
     data = {'noticias':noticias}
     return render(request, 'frikis/listar.html', data)


@login_required
def update_news(request, id):

    noticia= get_object_or_404(tusnoticias, id=id)

    data= {

        'form': EditaNoticia(instance=noticia)
    }
    
    if request.method == 'POST':
        formulario= EditaNoticia(data=request.POST, instance=noticia)  
        if formulario.is_valid():
          formulario.save()
          return redirect(to="listar")
        data["form"] = formulario  
    return render(request, 'frikis/modificar.html', data)

def credits(request):
    return render(request, 'frikis/credits.html')

def perfil(request):
    return render(request, 'frikis/perfil.html')

def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Mensaje enviado correctamente, Muchas gracias!")
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, "frikis/contact.html", context )

@login_required
def delete(request, tusnoticias_id):
    item = get_object_or_404(tusnoticias, id=tusnoticias_id)
    item.delete()
    return redirect('listar')

def nota (request, tusnoticias_id):
    noticia = get_object_or_404(tusnoticias, id=tusnoticias_id )
    context = {'noticia':noticia}
    return render(request, 'frikis/nota.html', context)