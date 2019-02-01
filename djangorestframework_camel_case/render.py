# -*- coding: utf-8 -*-
from rest_framework.renderers import BrowsableAPIRenderer

from djangorestframework_camel_case.settings import api_settings
from djangorestframework_camel_case.util import camelize


class CamelCaseJSONRenderer(api_settings.RENDERER_CLASS):
    def render(self, data, *args, **kwargs):
        return super(CamelCaseJSONRenderer, self).render(
            camelize(data), *args, **kwargs
        )


class CamelCaseBrowsableAPIRenderer(BrowsableAPIRenderer):
    def render(self, data, *args, **kwargs):
        return super(CamelCaseBrowsableAPIRenderer, self).render(
            camelize(data), *args, **kwargs
        )
