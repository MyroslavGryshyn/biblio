#!/usr/bin/env python3
from flask_script import Manager, Server

from src.server.app import create_app
from src.server.models import db, create_dummy_db

PATH_DUMMY_JSON = './dummy_data/dummy_data.json'

manager = Manager(create_app)
manager.add_command('runserver', Server(host='0.0.0.0', port='5000'))

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def dummy_db():
    create_dummy_db(PATH_DUMMY_JSON)

if __name__ == '__main__':
    manager.run()
