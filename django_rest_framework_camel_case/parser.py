# -*- coding: utf-8 -*-
import json

from django.conf import settings
from rest_framework.parsers import ParseError, six

from django_rest_framework_camel_case.settings import api_settings
from django_rest_framework_camel_case.util import underscoreize


class CamelCaseJSONParser(api_settings.PARSER_CLASS):
    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return underscoreize(
                json.loads(data),
                **api_settings.JSON_UNDERSCOREIZE
            )
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))
