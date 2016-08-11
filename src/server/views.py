from enum import Enum

from flask import jsonify, render_template, abort, request, send_file, make_response
from flask_restful import Resource

from src.server import models
from src.server.models import db


class Status(Enum):
    HTTP_200_OK = 200
    HTTP_201_CREATED = 201
    HTTP_202_ACCEPTED = 202
    HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
    HTTP_204_NO_CONTENT = 204
    HTTP_206_PARTIAL_CONTENT = 206

    HTTP_400_BAD_REQUEST = 400
    HTTP_401_UNAUTHORIZED = 401
    HTTP_403_FORBIDDEN = 403
    HTTP_404_NOT_FOUND = 404

    HTTP_500_INTERNAL_SERVER_ERROR = 500


class HelloWorld(Resource):
    def get(self):
        # headers = {'Content-Type': 'text/html'}
        # return make_response(
        #     render_template('index.html'),
        #     Status.HTTP_200_OK.value,
        #     headers)
        # return send_file('src/client/index.html')
        return make_response(open('src/client/index.html').read())


class Books(Resource):
    def get(self):
        books = models.Book.query.all()
        return jsonify([book.as_dict() for book in books])

    def post(self):
        # TODO validation of post data

        if not request.json:
            # abort(400)
            return None, Status.HTTP_400_BAD_REQUEST.value

        new_book = models.Book(
            request.json.get('book_name', None),
            request.json.get('book_author', 'None'),
            int(request.json.get('book_status', 0)),
            request.json.get('book_description', None))
        db.session.add(new_book)
        db.session.commit()
        return new_book.as_dict()


class Book(Resource):

    def get(self, id):
        # TODO error handler, when model for get not found
        detail_book = models.Book.query.get(id)

        if not detail_book:
            return None, Status.HTTP_204_NO_CONTENT.value

        return jsonify(detail_book.as_dict())

    def put(self, id):
        # TODO validation of post data

        if not request.json:
            return None, Status.HTTP_400_BAD_REQUEST.value

        modify_book = models.Book.query.get(id)
        modify_book.book_name = request.json.get('book_name', None)
        modify_book.book_author = request.json.get('book_author', 'None')
        modify_book.book_status = int(request.json.get('book_status', 0))
        modify_book.book_description = request.json.get('book_description', None)

        db.session.add(modify_book)
        db.session.commit()
        return modify_book.as_dict()

    def delete(self, id):
        remove_book = models.Book.query.get(id)

        if not remove_book:
            return None, Status.HTTP_204_NO_CONTENT.value

        db.session.delete(remove_book)
        db.session.commit()
        return None, Status.HTTP_200_OK.value
