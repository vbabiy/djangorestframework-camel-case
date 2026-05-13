from rest_framework.renderers import BrowsableAPIRenderer

from djangorestframework_camel_case.settings import api_settings
from djangorestframework_camel_case.util import camelize


class CamelCaseJSONRenderer(api_settings.RENDERER_CLASS):
    json_underscoreize = api_settings.JSON_UNDERSCOREIZE

    def render(self, data, *args, **kwargs):
        return super().render(
            camelize(data, **self.json_underscoreize), *args, **kwargs
        )


class CamelCaseBrowsableAPIRenderer(BrowsableAPIRenderer):
    json_underscoreize = api_settings.JSON_UNDERSCOREIZE

    def render(self, data, *args, **kwargs):
        return super(CamelCaseBrowsableAPIRenderer, self).render(
            camelize(data, **self.json_underscoreize), *args, **kwargs
        )
