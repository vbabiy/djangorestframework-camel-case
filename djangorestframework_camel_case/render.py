# -*- coding: utf-8 -*-
from djangorestframework_camel_case.settings import api_settings
from djangorestframework_camel_case.util import camelize


class CamelCaseJSONRenderer(api_settings.RENDERER_CLASS):
    def render(self, data, *args, **kwargs):
        return super(CamelCaseJSONRenderer, self).render(camelize(data), *args,
                                                         **kwargs)
