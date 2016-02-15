# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext as ctx
from django.contrib.sessions.models import Session
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Noticia
from .forms import NoticiaForm
from django.contrib.auth.decorators import login_required
import redis
import json


def home(request):
    noticias = Noticia.objects.all()
    return render_to_response('portal/home.html', locals(), context_instance=ctx(request))


def listado_paginas(request):
    ''' Vista para mostrar la tabla de las entradas creadas'''
    noticias = Noticia.objects.all()
    return render_to_response('portal/listado-pagina.html', locals(), context_instance=ctx(request))


@login_required(login_url=reverse_lazy('usuario:ingresar'))
def crear_pagina(request):
    ''' Vista para crear un entradas'''
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # form_json = {
    #     'titulo': form.cleaned_data.get('titulo'),
    #     'contenido': form.cleaned_data.get('contenido')
    # }

    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form_json = {
                'titulo': form.cleaned_data.get('titulo'),
                'contenido': form.cleaned_data.get('contenido')
            }
            r.publish('mundo', json.dumps(form_json))
            return redirect(reverse_lazy('noticia:listado_paginas'))
    else:
        form = NoticiaForm()
    return render_to_response('portal/crear-pagina.html', locals(), context_instance=ctx(request))


def ver_pagina(request, pk):
    ''' Vista ver el detalle de una pagina'''
    noticia = get_object_or_404(Noticia, pk=pk)
    return render_to_response('portal/ver-pagina.html', locals(), context_instance=ctx(request))
