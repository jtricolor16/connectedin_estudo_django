from django.db import models

# Create your models here.
from perfis.models import Perfil


class Notificacao(models.Model):
    areaTexto = models.CharField(max_length=128, null=False)
    perfil = models.ForeignKey(Perfil, related_name="notificacao")

    class Meta:
        ordering = ["-id"]
