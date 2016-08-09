import os

from flask import Flask

import settings


def create_app(config_module=settings.DevelopmentConfig):
    app = Flask('biblio')
    app.config.from_object(config_module)

    # _init_db(app)
    _init_views(app)
    return app


# def _init_db(app):
#     from src.server.models import db
#     db.create_all()

def _init_views(app):
    from src.server.views import add_resource
    add_resource(app)
