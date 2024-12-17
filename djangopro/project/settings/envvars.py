from djangopro.core.utils.collections import deep_update
from djangopro.core.utils.settings import get_setting_from_env
"""
Gather env variables with a matching prefix, strip out prefix, and adds it to global variables
"""

# globals() is a dict of global variables

deep_update(globals(), get_setting_from_env(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
