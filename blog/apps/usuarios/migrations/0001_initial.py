# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_login', models.DateTimeField(null=True, verbose_name=b'\xc3\x9altimo Login', blank=True)),
                ('usuario', models.CharField(unique=True, max_length=120, verbose_name=b'usuario')),
                ('email', models.EmailField(db_index=True, unique=True, max_length=60, blank=True)),
                ('password', models.CharField(max_length=64, verbose_name=b'Contrase\xc3\xb1a')),
                ('estado', models.BooleanField(default=True, verbose_name=b'Estado')),
            ],
            options={
                'ordering': ['usuario'],
            },
        ),
    ]
