# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext as ctx
from django.views.generic import CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone
from django.contrib import messages
from .models import Usuario
from .forms import IngresarForm
from apps.noticias.models import Noticia


class RegistroCreate(CreateView):
    ''' Vista para registrar usuario, se uso vistas basadas en clases '''
    model = Usuario
    fields = ['usuario', 'password', 'email']
    template_name = 'portal/registro.html'
    success_url = reverse_lazy('usuario:ingresar')


def ingresar(request):
    ''' Vista de login '''
    if request.method == "POST":
        form = IngresarForm(request.POST)
        if form.is_valid():
            user = form.auth()
            if user is not None:
                if user.estado:
                    user.last_login = timezone.now()
                    user.save()
                    login(request, user)
                    return redirect(reverse('noticia:crear_pagina'))
                else:
                    messages.add_message(request, messages.WARNING, 'Usuario no se encuentra registrado')
            else:
                messages.add_message(request, messages.WARNING, u'El email y contraseña son inválidos')
    else:
        form = IngresarForm()

    return render_to_response('portal/login.html', locals(), context_instance=ctx(request))
