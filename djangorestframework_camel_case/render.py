from rest_framework.renderers import BrowsableAPIRenderer

from djangorestframework_camel_case.settings import api_settings
from djangorestframework_camel_case.util import camelize


class CamelCaseJSONRenderer(api_settings.RENDERER_CLASS):
    """
    :param ignore_keys: a set of keys to whose values to ignore whilse recusrively trversing the data
    """
    def __init__(self, ignore_keys=None):
        self.ignore_keys = ignore_keys or set()
        super().__init__()

    def render(self, data, *args, **kwargs):
        return super().render(camelize(data, ignore_keys=self.ignore_keys), *args, **kwargs)


class CamelCaseBrowsableAPIRenderer(BrowsableAPIRenderer):
    def render(self, data, *args, **kwargs):
        return super(CamelCaseBrowsableAPIRenderer, self).render(
            camelize(data), *args, **kwargs
        )
