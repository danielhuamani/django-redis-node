# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(to='noticias.Noticia'),
        ),
    ]
