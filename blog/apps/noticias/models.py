from django.db import models
from django.core.urlresolvers import reverse
from apps.usuarios.models import Usuario


class CategoriaNoticia(models.Model):
    nombre = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Categoria Noticia"
        verbose_name_plural = "Categoria Noticias"

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    usuario = models.ForeignKey(Usuario)
    titulo = models.CharField(max_length=120)
    contenido = models.TextField()
    categoria = models.ForeignKey(CategoriaNoticia)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('noticia:ver_pagina', kwargs={'pk': self.pk})
