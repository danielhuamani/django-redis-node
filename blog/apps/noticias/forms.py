# -*- coding: utf-8 -*-
from .models import Noticia
from django import forms


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['contenido', 'titulo', 'categoria', 'usuario']
