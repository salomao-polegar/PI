from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name='indexLojista'),
    path("sair", views.sair, name='sair'),
    
    
    
]