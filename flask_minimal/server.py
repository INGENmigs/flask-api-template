from flask import Flask, request
from flask.ext.restful import Resource, Api, marshal_with, fields, abort
from flask_restful_swagger import swagger
from flask_minimal.api import IndexEndpoint
from flask_minimal.api import HelloEndpoint

API_VERSION_NUMBER = '1.0'
API_VERSION_LABEL = 'v1'


class CustomFlaskApp(object):

    def __init__(self):
        self.app = Flask(__name__)
        custom_errors = {
            'JsonInvalidError': {
                'status': 500,
                'message': 'JSON format not valid'
            },
            'JsonRequiredError': {
                'status': 400,
                'message': 'JSON input required'
            }
        }
        self.api = swagger.docs(Api(self.app, errors=custom_errors), apiVersion=API_VERSION_NUMBER)
        
        # These are how the endpoints are called
        self.api.add_resource(IndexEndpoint, '/', endpoint='index')
        self.api.add_resource(HelloEndpoint, '/hello', endpoint='hello')

    def run(self, *args, **kwargs):
        self.app.config['PROPAGATE_EXCEPTIONS'] = False
        self.app.run(*args, **kwargs)


def run_app(*args, **kwargs):
    app = CustomFlaskApp()
    app.run(*args, **kwargs)


if __name__ == '__main__':
    run_app(debug=True)
