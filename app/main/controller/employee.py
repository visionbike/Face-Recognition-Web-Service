from flask import request
from flask_restplus import Resource
from ..service import get_staff, add_employee, delete_employee, get_employee, update_employee
from ..dto import EmployeeDto

api = EmployeeDto.api
_employee = EmployeeDto.employee


@api.route('/')
class EmployeeList(Resource):
    @api.doc('Get all members of staff')
    @api.marshal_list_with(_employee, envelope='data')
    def get(self):
        """
        Get all members of staff
        """
        return get_staff()

    @api.doc('Create new employee')
    @api.response(201, 'Success to create new employee.')
    @api.response(400, 'Fail to create new employee.')
    @api.response(409, 'Employee already exists.')
    @api.expect(_employee, validate=True)
    def post(self):
        """
        Create new employee
        """
        data = request.json
        return add_employee(data=data)

    @api.doc('Update employee info')
    @api.response(200, 'Success to update employee.')
    @api.response(400, 'Fail to update employee.')
    @api.response(404, 'Not found employee.')
    @api.expect(_employee)
    def put(self):
        """
        Update employee info given its id
        """
        data = request.json
        return update_employee(data=data)


@api.route('/<string:id>')
@api.param('id', 'identifier', _in='query')
class Employee(Resource):
    @api.doc('Get employee info')
    @api.response(200, 'Success to get employee.')
    @api.response(404, 'Not found employee.')
    @api.marshal_with(_employee)
    def get(self, id):
        """
        Get employee given its id
        """
        response = get_employee(id)
        if not response:
            return api.abort(404, error='not found', message='Not found employee with id=\'{}\''.format(id))
        return response

    @api.doc('Delete employee')
    @api.response(200, 'Success to delete employee.')
    @api.response(404, 'Not found employee.')
    def delete(self, id):
        """
        Delete employee info given its id
        """
        return delete_employee(id)
