# -*- coding:UTF-8 -*-

from django import forms
from django.contrib.auth.models import User

class usuarioFormulario(forms.Form):
    nome=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    senha=forms.CharField(required=True)
    nascimento=forms.DateField(required=True)
    empresa = forms.CharField(required=True)
    telefone=forms.CharField(required=True)

class SalvarFormulario(usuarioFormulario):

    def is_valid(self):
        valid=True
        if not super(usuarioFormulario, self).is_valid():
            self.adiciona_erro("Erro ao salvar o usuário")
            valid= False

        user_exists = User.objects.filter(username=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Usuario ja existente')
            valid = False

        return valid

    def adiciona_erro(self, message):
        erros=self.errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        erros.append(message)

class EditarFormulario(usuarioFormulario):

    def is_valid(self):
        valid=True
        if not super(usuarioFormulario, self).is_valid():
            self.adiciona_erro("Erro ao Editar o usuário")
            valid= False

        return valid

    def adiciona_erro(self, message):
        erros=self.errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        erros.append(message)

class ImageUploadForm(forms.Form):
    """Image upload form."""
    foto = forms.ImageField()