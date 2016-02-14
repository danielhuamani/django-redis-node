# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaNoticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=120)),
                ('contenido', models.TextField()),
                ('categoria', models.ForeignKey(to='noticias.CategoriaNoticia')),
                ('usuario', models.ForeignKey(to='usuarios.Usuario')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]
