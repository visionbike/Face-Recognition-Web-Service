from flask_restplus import fields, Namespace, Model


class EmployeeDto(Namespace):
    api = Namespace('Employee', description='Employee related operations')
    employee = api.model('Employee', {'id': fields.String(description='identifier'),
                                      'name': fields.String(description='full name'),
                                      'dept': fields.String(description='department'),
                                      'email': fields.String(description='email'),
                                      'nimages': fields.Integer(description='number of images'),
                                      'created_on': fields.DateTime(description='created time'),
                                      'updated_on': fields.DateTime(description='updated time')})

    p_employee = Model('PrivateEmployee', {'id': fields.String(description='identifier')})

