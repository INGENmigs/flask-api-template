from flask import request
from flask.ext.restful import Resource, Api, marshal_with, fields, abort
from flask_restful_swagger import swagger
from .models import IndexResult
from .models import HelloResult
from .errors import JsonRequiredError
from .errors import JsonInvalidError

""" Each Class is used to process the output of the endpoints """

class IndexEndpoint(Resource):
    @swagger.operation(
        responseClass=IndexResult.__name__,
        nickname='index')
    @marshal_with(IndexResult.resource_fields)
    def get(self):
        return IndexResult()

    # I'm not yet too sure what some of these functions do yet.
    # But I assume @swagger calls the models
    # @marshal_with is a decorator
    # and OFC "def get()" is the GET Method


class HelloEndpoint(Resource):
    @swagger.operation(
        responseClass=HelloResult.__name__,
        nickname='hello',
        responseMessages=[
            {"code": 400, "message": "Input required"},
            {"code": 500, "message": "JSON format not valid"},
        ],
        parameters=[
            {
                "name": "name",
                "description": "JSON-encoded name",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "body"
            },
        ])
    @marshal_with(HelloResult.resource_fields)
    def post(self):
        """Return a HelloResult object"""
        reqs = request.get_json()
        if not reqs:
            raise JsonRequiredError()
        try:
            reqs['name']
            return HelloResult(name=reqs['name'])
        except KeyError:
            raise JsonInvalidError()
