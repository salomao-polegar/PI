from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", views.index),
    path('index/', views.index, name="index"),
    path('agendar/', views.agendar, name="agendar"),
    path('servico/', views.servico, name="servico"),
    path('servico/<str:id>', views.servico, name="servico")


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
