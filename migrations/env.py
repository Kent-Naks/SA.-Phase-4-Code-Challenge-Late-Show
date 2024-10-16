import logging
from logging.config import fileConfig

from flask import current_app
from alembic import context

# Alembic Config object for accessing the .ini file
config = context.config

# Setup Python logging configuration from the file
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

def get_engine():
    try:
        # Works with Flask-SQLAlchemy<3 and Alchemical
        return current_app.extensions['migrate'].db.get_engine()
    except (TypeError, AttributeError):
        # Works with Flask-SQLAlchemy>=3
        return current_app.extensions['migrate'].db.engine


def get_engine_url():
    try:
        return get_engine().url.render_as_string(hide_password=False).replace('%', '%%')
    except AttributeError:
        return str(get_engine().url).replace('%', '%%')
