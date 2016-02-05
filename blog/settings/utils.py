# -*- coding: utf-8 -*-

import json
from os.path import join


def get_env(base_dir):
    """ Obtiene las 'variables de configuración' desde un archivo json."""
    with open(join(base_dir, 'settings/configuracion.json')) as f:
        return json.load(f)
    return {}
