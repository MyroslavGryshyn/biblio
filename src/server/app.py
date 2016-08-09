import os

from flask import Flask

import settings

app = Flask('__name__')


def create_app(config_module=settings.DevelopmentConfig):
    app.config.from_object(config_module)

    _init_db(app)
    _init_views(app)
    return app


def _init_db(app):
    from src.server.models import db
    db.init_app(app)


def _init_views(app):
    from src.server.views import add_resource
    add_resource(app)
