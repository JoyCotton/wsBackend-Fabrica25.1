from django.contrib import admin
from django.urls import path
from RaM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PersonagemLista, name='personagem_lista'),
    path('catar/', views.CatarPersonagens, name='fetch_characters'),
    path('personagem/<int:pk>/', views.PersonagemDetalhe, name='personagem_detalhe'),
    path('personagem/new/', views.PersonagemCriar, name='personagem_criar'),
    path('personagem/<int:pk>/edit/', views.PersonagemUpdate, name='personagem_update'),
    path('personagem/<int:pk>/delete/', views.PersonagemDeletar, name='personagem_deletar'),
]