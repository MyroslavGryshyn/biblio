from flask import jsonify, render_template, make_response
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
        pass


class Book(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
