from flask import request, jsonify
from flask_restplus import Resource
from ..dto import TrainDto, EmployeeDto
from ..service import get_employee_ids
from ..util import selective_marshal_with

api = TrainDto.api


@api.route('/')
class Train(Resource):
    @api.doc('Train recognition model')
    @api.response(200, 'Success to train recognition model.')
    @api.response(400, 'Fail to train recognition model.')
    @selective_marshal_with(EmployeeDto.p_employee)
    def post(self):
        print(jsonify(get_employee_ids()))
        return get_employee_ids()
