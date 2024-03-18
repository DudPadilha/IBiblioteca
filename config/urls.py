"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('livros/', LivroView.as_view(), name='livros'),
    path('reserva/', EmprestimoView.as_view(),
name='reserva'),
    path('cidade/', CidadeView.as_view(),
name='cidade'),
    path('autor/', AutorView.as_view(), name='autor'),
    path('editor/', EditoraView.as_view(),
name='editora'),
    path('leitor/', UsuarioView.as_view(),
name='leitor'),
    path('genero/', GeneroView.as_view(),
name='genero'),
]
