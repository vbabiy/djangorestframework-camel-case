# -*- coding: utf-8 -*-

from django.conf import settings
from rest_framework.settings import APISettings

_rest_framework_settings = getattr(settings, 'REST_FRAMEWORK', None)

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
    'RENDERER_CLASS',
    'PARSER_CLASS'
)

DEFAULTS = {
    'RENDERER_CLASS': 'rest_framework.renderers.JSONRenderer',
    'PARSER_CLASS': 'rest_framework.parsers.JSONParser'
}

VALID_SETTINGS = {
    'RENDERER_CLASS': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'PARSER_CLASS': (
        'rest_framework.parsers.JSONParser',
    )
}


rest_framework_settings = APISettings(
    _rest_framework_settings, DEFAULTS, IMPORT_STRINGS
)
