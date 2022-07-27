from flask.ext.restful import Resource, Api, marshal_with, fields, abort
from flask_restful_swagger import swagger
 
# As comares to @swagger.operations in the main.py
# @swagger.model initializes the model i think so. 
@swagger.model
class IndexResult(object):
    """The result of a call to /dummy"""
    resource_fields = {
        'Homepage': fields.String
    }

    def __init__(self):
        self.Homepage = "HI!! This is to test the Homepage!"


@swagger.model
class HelloResult(object):
    """The result of a call to /hello"""
    resource_fields = {
        'greetings': fields.String
    }

    def __init__(self, name):
        self.greetings = "Hello {}".format(name)
        # Should output "greetings: Hello World" if POST method is succesful
        # and 'name' is set to "World"
