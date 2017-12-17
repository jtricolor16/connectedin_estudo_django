"""connectedin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from perfis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.perfis, name='perfis'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
    url(r'^perfis/pesquisar$', views.pesquisar_nome.as_view(), name='pesquisar'),
    url(r'^perfis/(?P<perfil_id>\d+)/excluir_contato$', views.excluir_contato, name='excluir_contato'),
    url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar_convite, name='aceitar'),
    url(r'^convite/(?P<convite_id>\d+)/recusar$', views.recusar_convite, name='recusar'),
    url(r'^perfis/editar$', views.editar_perfil, name='editar_perfil'),
]
