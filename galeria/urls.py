from django.urls import path

from .views import imagem, index

urlpatterns = [
    path('', index, name='home'),
    path('imagem/', imagem, name='imagem'),
]
