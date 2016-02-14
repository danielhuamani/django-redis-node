from django.db import models
from apps.noticias.models import Noticia


class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia)
    nombre = models.CharField(max_length=120)
    comentario = models.TextField()

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.nombre
