# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
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
        'rest_framework.renderers.UnicodeJSONRenderer',
    ),
    'PARSER_CLASS': (
        'rest_framework.parsers.JSONParser',
    )
}


def validate_settings(input_settings, valid_settings):
    for setting_name, valid_values in valid_settings.iteritems():
        input_setting = input_settings.get(setting_name)
        if input_setting and input_setting not in valid_values:
            raise ImproperlyConfigured(setting_name)


validate_settings(_rest_framework_settings, VALID_SETTINGS)

rest_framework_settings = APISettings(
    _rest_framework_settings, DEFAULTS, IMPORT_STRINGS
)
