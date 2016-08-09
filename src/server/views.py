from flask_restful import Resource, Api


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

def add_resource(app):
    api = Api(app)
    api.add_resource(HelloWorld, '/')
