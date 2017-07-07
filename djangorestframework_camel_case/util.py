import re
from collections import OrderedDict

from django.utils import six

first_cap_re = re.compile(r'(.)([A-Z]|[0-9]+)')
all_cap_re = re.compile(r'([a-z]|[0-9]+[a-z]?|[A-Z]?)([A-Z0-9])')
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
    if isinstance(data, (list, tuple)):
        return [camelize(item) for item in data]
    return data


def camel_to_underscore(name):
    return all_cap_re.sub(r'\1_\2', name).lower()


def underscoreize(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            if isinstance(key, six.string_types):
                new_key = camel_to_underscore(key)
            else:
                new_key = key
            new_dict[new_key] = underscoreize(value)
        return new_dict
    if isinstance(data, (list, tuple)):
        return [underscoreize(item) for item in data]

    return data
