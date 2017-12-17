from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from notificacao.forms import notificacaoForm
from notificacao.models import Notificacao


class notificacaoView(View):

    def get(self, request):
        pass

    def post(self, request):

        form = notificacaoForm(request.POST)

        if(form.is_valid()):

            dados_form = form.data

            notificacao = Notificacao(areaTexto=dados_form['areaTexto'], perfil=request.user.perfil)

            notificacao.save()

            return redirect('index')




