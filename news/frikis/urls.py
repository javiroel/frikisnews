from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:tusnoticias_id>/', views.noticias, name='noticias'),
    path('crearnoticia/',views.creanews, name='creanews'),
    path('login/',views.login, name='login'),
    path('registro/',views.registro, name='registro'),
    path('listar/', views.listar, name='listar'),
    path('modificar/<int:tusnoticias_id>', views.edit, name='modificar'),
]
