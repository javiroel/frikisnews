from django.urls import path
from .views import crear_perfil, edita_perfil, perfil_usuario

urlpatterns = [
    # Otras URLs de tu aplicación aquí
    path('', perfil_usuario, name='perfil_usuario'),
    path('crearperfil/', crear_perfil, name='crear_perfil'), 
    path('editarperfil/', edita_perfil, name='editar_perfil')
]
