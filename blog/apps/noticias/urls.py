# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^crear_pagina/$', views.crear_pagina, name='crear_pagina'),
    url(r'^ver-pagina/(?P<pk>\d+)/$', views.ver_pagina, name='ver_pagina'),
    url(r'^listado_paginas/$', views.listado_paginas, name='listado_paginas'),
]
