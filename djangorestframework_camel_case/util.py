import re
from collections import OrderedDict

from django.core.files import File
from django.http import QueryDict
from django.utils.encoding import force_text
from django.utils.functional import Promise

from rest_framework.utils.serializer_helpers import ReturnDict

camelize_re = re.compile(r"[a-z0-9]?_[a-z0-9]")


def underscore_to_camel(match):
    group = match.group()
    if len(group) == 3:
        return group[0] + group[2].upper()
    else:
        return group[1].upper()


def camelize(data, ignore_keys=None):
    ignore_keys = ignore_keys or set()
    # Handle lazy translated strings.
    if isinstance(data, Promise):
        data = force_text(data)
    if isinstance(data, dict):
        if isinstance(data, ReturnDict):
            new_dict = ReturnDict(serializer=data.serializer)
        else:
            new_dict = OrderedDict()
        for key, value in data.items():
            if isinstance(key, Promise):
                key = force_text(key)
            if isinstance(key, str) and "_" in key:
                new_key = re.sub(camelize_re, underscore_to_camel, key)
            else:
                new_key = key

            # recurse and modify contents if key/field not ignored
            if new_key not in ignore_keys and key not in ignore_keys:
                new_dict[new_key] = camelize(value, ignore_keys)
            else:
                new_dict[new_key] = value

        return new_dict
    if is_iterable(data) and not isinstance(data, str):
        return [camelize(item, ignore_keys) for item in data]
    return data


def get_underscoreize_re(options):
    if options.get("no_underscore_before_number"):
        pattern = r"([a-z0-9]|[A-Z]?(?=[A-Z](?=[a-z])))([A-Z])"
    else:
        pattern = r"([a-z0-9]|[A-Z]?(?=[A-Z0-9](?=[a-z0-9]|$)))([A-Z]|(?<=[a-z])[0-9](?=[0-9A-Z]|$)|(?<=[A-Z])[0-9](?=[0-9]|$))"
    return re.compile(pattern)


def camel_to_underscore(name, **options):
    underscoreize_re = get_underscoreize_re(options)
    return underscoreize_re.sub(r"\1_\2", name).lower()


def _get_iterable(data):
    if isinstance(data, QueryDict):
        return data.lists()
    else:
        return data.items()


def underscoreize(data, ignore_keys=None, **options):
    ignore_keys = ignore_keys or set()
    if isinstance(data, dict):
        new_dict = {}
        for key, value in _get_iterable(data):
            if isinstance(key, str):
                new_key = camel_to_underscore(key, **options)
            else:
                new_key = key

            # recurse and modify contents if key/field not ignored
            if new_key not in ignore_keys and key not in ignore_keys:
                new_dict[new_key] = underscoreize(value, ignore_keys, **options)
            else:
                new_dict[new_key] = value

        if isinstance(data, QueryDict):
            new_query = QueryDict(mutable=True)
            for key, value in new_dict.items():
                new_query.setlist(key, value)
            return new_query
        return new_dict
    if is_iterable(data) and not isinstance(data, (str, File)):
        return [underscoreize(item, ignore_keys, **options) for item in data]

    return data


def is_iterable(obj):
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return True
