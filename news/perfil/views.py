from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from perfil.forms import UserProfileForm

from perfil.forms import EditarPerfilForm
from .models import UserProfile

@login_required
def crear_perfil(request):
    if request.method == 'POST':
        user=request.user
        # Crea el perfil de usuario
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
          user_profile = form.save(commit=False)
          user_profile.user = user
          user_profile.save()
        return redirect('perfil_usuario')  # Redirige a donde desees después de crear el perfil de usuario
    
    else:
        # Renderiza el formulario de creación de perfil
        context = {'form': UserProfileForm()} 
        return render(request, 'perfil/crear_perfil.html', context)

# Vista de perfil de usuario
from .models import UserProfile

@login_required
def perfil_usuario(request):

    if UserProfile.objects.filter(user=request.user).exists():
     user_profile = UserProfile.objects.get(user=request.user)
     context = {'user_profile': user_profile}
     print(context.keys())
     return render(request, 'perfil/perfil_usuario.html', context)
    
    else:
     return redirect('crear_perfil')  # Redirige a donde desees después de crear el perfil de usuario

@login_required

def edita_perfil(request):
  
  perfil=UserProfile.objects.get(user=request.user)
      
  data ={
      
      'form': EditarPerfilForm(instance=perfil)
      

  }

  if request.method == 'POST':
      formulario = EditarPerfilForm(data=request.POST, files=request.FILES, instance=perfil)
      if formulario.is_valid():
          formulario.save()
          return redirect(to="perfil_usuario")
      data["form"] = formulario
  return render(request, 'perfil/editar_perfil.html', data)       







