#!/usr/bin/env python3
from flask_script import Manager, Server

from src.server.app import create_app
# from src.server.models import db


manager = Manager(create_app)
manager.add_command('runserver', Server(host='0.0.0.0'))


# @manager.command
# def create_db():
#     db.create_all()
#
#
# @manager.command
# def drop_db():
#     db.drop_all()


if __name__ == '__main__':
    manager.run()