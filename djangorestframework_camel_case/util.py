import inflection
from collections import OrderedDict


def camelize(data):
    if isinstance(data, dict):
        new_dict = OrderedDict()

        for k, v in data.items():
            new_dict[inflection.camelize(k, uppercase_first_letter=False)] = camelize(v)

        return new_dict

    if isinstance(data, list):
        return [camelize(x) for x in data]

    if isinstance(data, tuple):
        return tuple(camelize(x) for x in data)

    return data


def underscoreize(data):
    if isinstance(data, dict):
        return {inflection.underscore(k): underscoreize(v) for k, v in data.items()}

    if isinstance(data, list):
        return [underscoreize(x) for x in data]

    if isinstance(data, tuple):
        return tuple(underscoreize(x) for x in data)

    return data
