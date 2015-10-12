import re

from collections import OrderedDict


def camelize_key(string, uppercase_first_letter=True):
    """
    From: https://github.com/jpvanhal/inflection

    Convert strings to CamelCase.
    Examples::
        >>> camelize("device_type")
        "DeviceType"
        >>> camelize("device_type", False)
        "deviceType"
    :func:`camelize` can be though as a inverse of :func:`underscore`, although
    there are some cases where that does not hold::
        >>> camelize(underscore("IOError"))
        "IoError"
    :param uppercase_first_letter: if set to `True` :func:`camelize` converts
        strings to UpperCamelCase. If set to `False` :func:`camelize` produces
        lowerCamelCase. Defaults to `True`.
    """
    if uppercase_first_letter:
        return re.sub(r"(?:^|_)(.)", lambda m: m.group(1).upper(), string)
    else:
        return string[0].lower() + camelize_key(string)[1:]


def underscore_key(string):
    """
    From: https://github.com/jpvanhal/inflection

    Make an underscored, lowercase form from the expression in the string.
    Example::
        >>> underscore("DeviceType")
        "device_type"
    As a rule of thumb you can think of :func:`underscore` as the inverse of
    :func:`camelize`, though there are cases where that does not hold::
        >>> camelize(underscore("IOError"))
        "IoError"
    """
    string = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', string)
    string = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', string)
    string = string.replace("-", "_")
    return string.lower()


def camelize(data):
    if isinstance(data, dict):
        new_dict = OrderedDict()

        for k, v in data.items():
            new_dict[camelize_key(k, False)] = camelize(v)

        return new_dict

    if isinstance(data, list):
        return [camelize(x) for x in data]

    if isinstance(data, tuple):
        return tuple(camelize(x) for x in data)

    return data


def underscoreize(data):
    if isinstance(data, dict):
        new_dict = dict()
        for key, value in data.items():
            new_dict[underscore_key(key)] = underscoreize(value)
        return new_dict

    if isinstance(data, list):
        return [underscoreize(x) for x in data]

    if isinstance(data, tuple):
        return tuple(underscoreize(x) for x in data)

    return data
