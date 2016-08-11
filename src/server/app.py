import os

from flask import Flask

import settings

app = Flask('__name__',
            template_folder=settings.DevelopmentConfig.template_dir,
            static_folder=settings.DevelopmentConfig.static_folder)


def create_app(config_module=settings.DevelopmentConfig):
    app.config.from_object(config_module)

    _init_db(app)
    _init_views(app)
    return app


def _init_db(app):
    from src.server.models import db
    db.init_app(app)


def _init_views(app):
    from src.server.urls import add_resource
    add_resource(app)
