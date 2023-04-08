
from django.shortcuts import render, redirect
from mensaje.forms import MensajeForm
from .models import Mensaje
from django.contrib.auth.decorators import login_required

@login_required

def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('outbox')  
    else:
        form = MensajeForm(initial={'remitente': request.user})
    return render(request, 'mensaje/enviar_mensaje.html', {'form': form})

@login_required

def inbox(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensaje/inbox.html', {'mensajes': mensajes})

@login_required

def outbox(request):
    mensajes = Mensaje.objects.filter(remitente=request.user)
    return render(request, 'mensaje/outbox.html', {'mensajes': mensajes})