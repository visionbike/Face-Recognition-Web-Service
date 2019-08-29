# from .main import api
# from .main.controller import EmployeeList, Employee
from flask import Blueprint
from flask_restplus import Api
from .main.controller import employee_ns, face_ns, train_ns

# api.add_resource(EmployeeList, '/employee/')
# api.add_resource(Employee, '/employee/<string:id>', endpoint='<string:id>')

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='Lac Viet Face Recognition API',
          description='',
          version='1.0.0',
          doc='/docs/')
api.add_namespace(employee_ns, path='/employee')
api.add_namespace(face_ns, path='/face')
api.add_namespace(train_ns, path='/train')