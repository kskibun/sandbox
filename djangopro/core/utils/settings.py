import os

from .misc import yaml_coerce


def get_setting_from_env(prefix):
    """
    acquire settings from environment
    """
    prefix_len = len(prefix)

    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
