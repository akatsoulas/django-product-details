"""
When this module is imported, we load all the .json files and insert them as
module attributes using locals().  It's a magical and wonderful process.
"""
import json
import os

from django.conf import settings

from . import settings_defaults


def settings_fallback(key):
    """Grab user-defined settings, or fall back to default."""
    return getattr(settings, key, getattr(settings_defaults, key))


json_dir = settings_fallback('PROD_DETAILS_DIR')

for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        name = os.path.splitext(filename)[0]
        path = os.path.join(json_dir, filename)
        locals()[name] = json.load(open(path))