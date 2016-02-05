# -*- coding: utf-8 -*-
from django.db import models


class Usuario(models.Model):
    last_login = models.DateTimeField('Último Login', blank=True, null=True)
    usuario = models.CharField("usuario", max_length=120, unique=True)
    email = models.EmailField(max_length=60, unique=True, db_index=True, blank=True)
    password = models.CharField(max_length=64, verbose_name='Contraseña')
    estado = models.BooleanField("Estado", default=True)

    class Meta:
        ordering = ['usuario']

    def __unicode__(self):
        return self.usuario

    def is_authenticated(self):
        return True

    @property
    def is_staff(self):
        return False
