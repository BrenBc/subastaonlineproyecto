from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('usuario/', views.usuario, name='user'),
    path('subasta/<str:pk>/', views.subasta, name='auction'),
    path('login/', views.iniciosesion, name="login"),
    path('logout/', views.cerrarsesion, name="logout"),

]
