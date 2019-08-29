from datetime import datetime
from flask import jsonify
from app.main.model import Employee
from app.main.util import insert, commit, delete
from app.main.util import code_200, code_201, code_400, code_404, code_409


def get_staff():
    return Employee.query.all()


def reset_all_nfaces():
    employees = Employee.query.all()
    if employees:
        for employee in employees:
            employee.nimages = 0
            commit()


def get_employee(id):
    return Employee.query.get(id)


def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        response = code_404('Not found employee with id=\'{}\''.format(id))
    else:
        delete(employee)
        response = code_200('Success to delete employee with id=\'{}\''.format(id))
    return response


def get_nfaces(id):
    employee = Employee.query.get(id)
    if employee:
        return employee.nimages
    return -1


def increase_nfaces(id):
    employee = Employee.query.get(id)
    if employee:
        employee.nimages += 1
        commit()


def decrease_nfaces(id):
    employee = Employee.query.get(id)
    if employee:
        employee.nimages = employee.nimages - 1 if employee.nimages > 0 else 0
        commit()


def reset_nfaces(id):
    employee = Employee.query.get(id)
    if employee:
        employee.nimages = 0
        commit()


def add_employee(data):
    employee = Employee.query.filter_by(id=data['id']).first()
    if not employee:
        if ('created_on' or 'updated_on' or 'nimages') in data.keys():
            response = code_400('Fail to add new employee with id=\'{}\'. Do not include `nimages`, `create_on` and `updated_on` in request body.'.format(data['id']))
        else:
            new_employee = Employee(id=data['id'], name=data['name'], dept=data['dept'], email=data['email'])
            insert(new_employee)
            response = code_201('Success to add new employee with id=\'{}\''.format(data['id']))
    else:
        response = code_409('Employee with id=\'{}\' already exists'.format(data['id']))
    return response


def update_employee(data):
    employee = Employee.query.get(data['id'])
    if not employee:
        response = code_404('Not found employee with id=\'{}\''.format(data['id']))
    else:
        if ('created_on' or 'updated_on' or 'nimages') in data.keys():
            response = code_400('Error to update employee info with id=\'{}\'. Do not include `create_on` and `updated_on` in request body.'.format(data['id']))
        else:
            for k in data.keys():
                if k == 'id':
                    continue
                setattr(employee, k, data[k])
            employee.updated_on = datetime.utcnow()
            commit()
            response = code_200('Success to update employee info with id=\'{}\''.format(data['id']))
    return response


def get_employee_ids():
    return Employee.query.all()

