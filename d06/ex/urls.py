from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    re_path(r'^$', views.accueil, name='accueil'),
    re_path('accueil', views.accueil, name='accueil'),
    path('inscription', views.inscription, name='inscription'),
   	path('connexion', views.connexion, name='connexion'),
]
