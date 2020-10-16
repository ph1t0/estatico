from pkg_resources import resource_filename
from pathlib import Path

FLASK_APP = resource_filename('estatico', '__init__.py')
TEMPLATES_PATH = Path(resource_filename('estatico', 'templates'))
