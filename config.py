import os
import sys


try:
    import local_config
except ImportError:
    for key, value in os.environ.items():
        setattr(sys.modules[__name__], key, value)
else:
    for attribute in dir(local_config):
        if attribute[:2] != '__' and attribute[-2:] != '__':
            setattr(sys.modules[__name__], attribute, getattr(local_config, attribute))

