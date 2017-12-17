from django.shortcuts import render, redirect
from django import forms
from usuarios.forms import *
from perfis.models import *
# Create your views here.
from django.views.generic.base import View
from django.contrib.auth.models import User

class RegistroUsuariosView(View):

    template_registro = 'registro.html'

    def get(self, request):
        return render(request, self.template_registro)

    def post(self, request):
        form = SalvarFormulario(request.POST)

        form_img = ImageUploadForm(request.POST or None, request.FILES or None)

        if form.is_valid() and form_img.is_valid():

            dados_form = form.data

            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])

            perfil = Perfil(nome=dados_form['nome'],
                            nascimento=dados_form['nascimento'],
                            telefone=dados_form['telefone'],
                            empresa=dados_form['empresa'],
                            foto=form_img.cleaned_data['foto'],
                            usuario=usuario)

            perfil.save()

            return redirect('index')

        return render(request, self.template_registro, {'form': form})

class EditarUsuariosView(View):

    template_edicao = 'editar.html'

    def get(self, request):
        return render(request, self.template_edicao)

    def post(self, request):
        form = EditarFormulario(request.POST)

        dados_form = form.data

        form_img = ImageUploadForm(request.POST or None, request.FILES or None)

        perfil = Perfil.objects.get(nome=dados_form['nome'])

        if form.is_valid() and form_img.is_valid():
            usuario = User.objects.get_by_natural_key(dados_form['nome'])
            perfil.telefone=dados_form['telefone']
            perfil.empresa=dados_form['empresa']
            perfil.foto = form_img.cleaned_data['foto']
            perfil.usuario=usuario

            perfil.save()


            return redirect('index')

        return render(request, self.template_edicao, {'form': form, 'perfil_logado' : perfil, 'data' : dados_form['nascimento']})
