# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, 'JSON_CAMEL_CASE', {})

DEFAULTS = {
    'RENDERER_CLASS': 'rest_framework.renderers.JSONRenderer',
    'PARSER_CLASS': 'rest_framework.parsers.JSONParser',

    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': False,
    },
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
    'RENDERER_CLASS',
    'PARSER_CLASS'
)

VALID_SETTINGS = {
    'RENDERER_CLASS': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.UnicodeJSONRenderer',
        'rest_framework_google_json_style_api.renderers.JSONRenderer',
        'rest_framework_json_api.renderers.JSONRenderer',
    ),
    'PARSER_CLASS': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_google_json_style_api.parsers.JSONParser',
        'rest_framework_json_api.parsers.JSONParser',
    )
}


def validate_settings(input_settings, valid_settings):
    for setting_name, valid_values in valid_settings.items():
        input_setting = input_settings.get(setting_name)
        if input_setting and input_setting not in valid_values:
            raise ImproperlyConfigured(setting_name)


validate_settings(USER_SETTINGS, VALID_SETTINGS)

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
