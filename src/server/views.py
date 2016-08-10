from flask import jsonify, render_template, make_response, abort
from flask_restful import Resource

from src.server import models


class HelloWorld(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)


class Books(Resource):
    def get(self):
        books = models.Book.query.all()
        return jsonify([book.as_dict() for book in books])

    def post(self):
        # TODO validation of post data
        pass


class Book(Resource):
    def get(self, id):
        # TODO error handler, when model for get not found
        book = models.Book.query.get(id)
        if not book:
            abort(404)
        return jsonify(book.as_dict())

    def put(self):
        pass

    def delete(self):
        pass
