# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registro/$', views.RegistroCreate.as_view(), name='registro'),

    url(r'^ingresar/$', views.ingresar, name='ingresar'),
]
