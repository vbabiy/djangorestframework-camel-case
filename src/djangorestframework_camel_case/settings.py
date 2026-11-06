from django.conf import settings
from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, "JSON_CAMEL_CASE", {})

DEFAULTS = {
    "RENDERER_CLASS": "rest_framework.renderers.JSONRenderer",
    "PARSER_CLASS": "rest_framework.parsers.JSONParser",
    "JSON_UNDERSCOREIZE": {"no_underscore_before_number": False, "ignore_fields": None, "ignore_keys": None},
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = ("RENDERER_CLASS", "PARSER_CLASS")

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
