import json

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.server.app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

def create_dummy_db(path_json):
    with open(path_json, 'r') as json_file:
        data = json.loads(json_file.read())
    for book in data['books']:
        current_book = Book(book['name'], book['author'], int(book['status']))
        db.session.add(current_book)
        db.session.commit()


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True)
    book_author = db.Column(db.String(120), unique=True)
    book_status = db.Column(db.Boolean, unique=False, default=True)

    def __init__(self, book_name, book_author, book_status):
        self.book_name = book_name
        self.book_author = book_author
        self.book_status = book_status

    def as_dict(self):
        book_as_dict = {}
        book_as_dict['book_name'] = self.book_name
        book_as_dict['book_author'] = self.book_author
        book_as_dict['book_status'] = self.book_status
        return book_as_dict
