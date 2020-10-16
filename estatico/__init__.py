import os
from configparser import ConfigParser
from flask import Flask
from importlib import import_module
from pkg_resources import resource_filename


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        config_parser = ConfigParser()
        settings_user_file = os.environ.get('APPLICATION_SETTINGS')

        if settings_user_file:
            config_parser.read(settings_user_file)
        else:
            config_parser.read(resource_filename('estatico', 'config.cfg'))
        for section in config_parser.sections():
            for option in config_parser.options(section):
                try:
                    value = config_parser.getboolean(section, option)
                except ValueError:
                    value = config_parser.get(section, option)
                app.config['{}_{}'.format(section, option)] = value

        blue_app = getattr(import_module('estatico.{}'.format(app.config['site_type'])), 'blueapp')
        app.register_blueprint(blue_app)
    else:
        app.config.from_mapping(test_config)

    return app
