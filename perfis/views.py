from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View
import datetime
from notificacao.models import Notificacao
from perfis.forms import pesquisar
from perfis.models import Perfil, Convite


@login_required
def index(request):
    notificacoes = get_perfil_logado(request).get_notificacoes()
    return render(request, 'index.html', {'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request), 'notificacoes' : notificacoes})

@login_required
def perfis(request, perfil_id):
    perfil=Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', {"perfil" : perfil, 'perfil_logado' : get_perfil_logado(request)})


@login_required
def convidar(request, perfil_id):
    # if (not request.user.has_perm("perfis.add_convite")):
    #     return render(request, 'index.html', {'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request), 'permissao_negada': 'Permissão Negada'})
    perfil_convidado=Perfil.objects.get(id=perfil_id)
    solicitante=get_perfil_logado(request)
    solicitante.convidar(perfil_convidado)
    return redirect('index')

@login_required
def get_perfil_logado(request):
    return request.user.perfil

@login_required
def aceitar_convite(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

@login_required
def recusar_convite(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.recusar()
    return redirect('index')

@login_required
def editar_perfil(request):
    perfil=get_perfil_logado(request)
    DATE_FORMAT = "%Y-%m-%d"
    data_string = perfil.nascimento.strftime(DATE_FORMAT)
    return render(request, 'editar.html', {'perfil_logado' : get_perfil_logado(request), 'data' : data_string})

@login_required
def excluir_contato(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    get_perfil_logado(request).excluir_contato(perfil)
    return redirect('index')

class pesquisar_nome(View):
    def get(self, request):
        form = pesquisar(request.GET)

        pesquisa_form=form.data

        perfis = Perfil.objects.filter(nome__startswith=pesquisa_form['texto'])

        return render(request, "pesquisar.html", {'perfis': perfis, 'perfil_logado' : get_perfil_logado(request)})





