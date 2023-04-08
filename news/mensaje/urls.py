from django.urls import path
from .views import inbox, enviar_mensaje, outbox

urlpatterns = [
    # Otras URLs de tu aplicación...
    path('', inbox, name='inbox'),
    path('outbox/', outbox, name='outbox'),
    path('enviar_mensaje/', enviar_mensaje, name='enviar_mensaje'),
]
