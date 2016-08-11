from flask_restful import Api

from src.server.views import HelloWorld, Books, Book, GetPartialStatic


def add_resource(app):
    api = Api(app)
    api.add_resource(HelloWorld, '/', endpoint='hello')
    api.add_resource(Books, '/api/v1/books/', endpoint='books')
    api.add_resource(Book, '/api/v1/books/<int:id>', endpoint='book')
    api.add_resource(GetPartialStatic, '/partial/<path:file_path>', endpoint='partial')
