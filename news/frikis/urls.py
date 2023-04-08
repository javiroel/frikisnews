import statistics
from django.urls import path
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('perfil/', views.perfil, name='perfil'),
    path('creditos/', views.credits, name='creditos'),
    path('crearnoticia/',views.creanews, name='creanews'),
    path('login/',views.login, name='login'),
    path('registro/',views.registro, name='registro'),
    path('listar/', views.listar, name='listar'),
    path('nota/<int:tusnoticias_id>', views.nota, name='nota'),
    path('modificar/<int:tusnoticias_id>', views.edit, name='modificar'),
    path('updatenoticia/<int:id>/', views.update_news, name='updatenoticia'),
    path('contact/',views.contact_view , name='contact'),
    path('delete/<int:tusnoticias_id>', views.delete, name='delete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
