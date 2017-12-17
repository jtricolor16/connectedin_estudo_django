from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.dateparse import parse_date


class Perfil(models.Model):
    nome=models.CharField(max_length=255, null=False)
    nascimento=models.DateField(null=False)
    telefone=models.CharField(max_length=255)
    empresa=models.CharField(max_length=255)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name='perfil')
    foto = models.ImageField(upload_to='', default='none.jpg')

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, convidado):
        return Convite.objects.create(solicitante=self, convidado=convidado)

    def convites_recebidos(self):
        return Convite.objects.filter(convidado__id=self.id)

    def convites_enviados(self):
        return Convite.objects.filter(solicitante__id=self.id)

    def convidados(self):
        convites = Convite.objects.filter(solicitante__id=self.id)
        convidados = [convite.convidado for convite in convites if convite.solicitante.id==self.id]
        return convidados

    def excluir_contato(self, contato):
        self.contatos.remove(contato)
        contato.contatos.remove(self)
        self.save()

    def get_notificacoes(self):
        return self.notificacao


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='solicitante')
    convidado = models.ForeignKey(Perfil, related_name='convidado')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()

    def recusar(self):
        self.delete()