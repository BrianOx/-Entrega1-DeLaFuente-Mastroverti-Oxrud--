from django.urls import path
from .views import *


urlpatterns = [
   path('campeones/', campeones, name='campeones'),
   path('buscar-campeon/', buscar_campeon, name='buscar-campeon'),
   path('items/', items, name='items'),
   path('posteos/', posteos, name='posteos'),
   path('formulario-posteo/',formulario_posteo, name='formulario-posteo'),
   path('insertar-posteo/',insertar_posteo, name='insertar-post'),
   path('', inicio, name='inicio'),
]

