import os
from estatico import create_app
from configparser import ConfigParser


config = """
[site]
type = website
test = default

[static]
test = true
"""


def test_user_configs():
    config_parser = ConfigParser()
    config_parser.read_string(config)

    with open('test_config.cfg', 'w') as configfile:
        config_parser.write(configfile)
    os.environ['APPLICATION_SETTINGS'] = 'test_config.cfg'

    app = create_app()

    os.remove('test_config.cfg')
    os.environ.pop('APPLICATION_SETTINGS')

    assert app.config['site_test'] == 'default'
    assert app.config['static_test']
    assert not app.config['static_test'] == 'true'
