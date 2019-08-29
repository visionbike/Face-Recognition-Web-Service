from flask import jsonify


def code_200(message):
    response = jsonify({'status': 'ok', 'message': message})
    response.status_code = 200
    return response


def code_201(message):
    response = jsonify({'status': 'created', 'message': message})
    response.status_code = 201
    return response


def code_202(message):
    response = jsonify({'status': 'accepted', 'message': message})
    response.status_code = 202
    return response


def code_400(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def code_401(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def code_403(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def code_404(message):
    response = jsonify({'error': 'not found', 'message': message})
    response.status_code = 404
    return response


def code_405(message):
    response = jsonify({'error': 'method not allowed', 'message': message})
    response.status_code = 405
    return response


def code_409(message):
    response = jsonify({'error': 'conflict', 'message': message})
    response.status_code = 409
    return response


def code_500(message):
    response = jsonify({'error': 'internal server error', 'message': message})
    response.status_code = 500
    return response
