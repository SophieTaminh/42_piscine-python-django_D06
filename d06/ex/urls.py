from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    re_path(r'^$', views.accueil, name='accueil'),
]
