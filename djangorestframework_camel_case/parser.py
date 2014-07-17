# -*- coding: utf-8 -*-
import json

from rest_framework.parsers import JSONParser, ParseError, six
from django.conf import settings
from djangorestframework_camel_case.util import underscoreize


class CamelCaseJSONParser(JSONParser):
    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return underscoreize(json.loads(data))
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))
