import re
from collections import OrderedDict

from django.core.files import File
from django.http import QueryDict
from django.utils import six

camelize_re = re.compile(r"[a-z0-9]?_[a-z0-9]")


def underscore_to_camel(match):
    group = match.group()
    if len(group) == 3:
        return group[0] + group[2].upper()
    else:
        return group[1].upper()


def camelize(data):
    if isinstance(data, dict):
        new_dict = OrderedDict()
        for key, value in data.items():
            if isinstance(key, six.string_types) and '_' in key:
                new_key = re.sub(camelize_re, underscore_to_camel, key)
            else:
                new_key = key
            new_dict[new_key] = camelize(value)
        return new_dict
    if is_iterable(data) and not isinstance(data, six.string_types):
        return [camelize(item) for item in data]
    return data


def get_underscoreize_re(options):
    if options.get('no_underscore_before_number'):
        pattern = r'([a-z]|[0-9]+[a-z]?|[A-Z]?)([A-Z])'
    else:
        pattern = r'([a-z]|[0-9]+[a-z]?|[A-Z]?)([A-Z0-9])'
    return re.compile(pattern)


def camel_to_underscore(name, **options):
    underscoreize_re = get_underscoreize_re(options)
    return underscoreize_re.sub(r'\1_\2', name).lower()


def _get_iterable(data):
    if isinstance(data, QueryDict):
        return data.lists()
    else:
        return data.items()

def underscoreize(data, **options):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in _get_iterable(data):
            if isinstance(key, six.string_types):
                new_key = camel_to_underscore(key, **options)
            else:
                new_key = key
            new_dict[new_key] = underscoreize(value, **options)

        if isinstance(data, QueryDict):
            new_query = QueryDict(mutable=True)
            for key, value in new_dict.items():
                new_query.setlist(key, value)
            return new_query
        return new_dict
    if is_iterable(data) and not isinstance(data, (six.string_types, File)):
        return [underscoreize(item, **options) for item in data]

    return data


def is_iterable(obj):
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return True
