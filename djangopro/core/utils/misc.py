import yaml


def yaml_coerce(value):
    """ Convert given value to valid python"""
    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
