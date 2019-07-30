"""
Face Recognition Service
Error Handling

Copyright (c) 2019 Nguyen Thanh Thien Phuc
Licensed under the MIT License (see LICENSE for details)
"""
from flask import jsonify, request, render_template
from . import api


def bad_request_error_handler(message):
    """
    Bad Request error handler
    :param message: error message
    """
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized_error_handler(message):
    """
    Unauthorized error handler
    :param message: error message
    """
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden_error_handler(message):
    """
    Forbidden error handler
    :param message: error message
    """
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@api.app_errorhandler(403)
def forbidden(e):
    """
    Forbidden error handler with HTTP content negotiation
    """
    if request.accept_mimetypes.accrpt_json and not request.accept_mimetypes.accept_html:
        response = jsonify('error', 'forbidden')
        response.status_code = 403
        return response
    return render_template('403.html'), 403


@api.app_errorhandler(404)
def page_notfound(e):
    """
    Not Found error handler with HTTP content negotiation
    """
    if request.accept_mimetypes.accrpt_json and not request.accept_mimetypes.accept_html:
        response = jsonify('error', 'not found')
        response.status_code = 404
        return response
    return render_template('404.html'), 404


@api.app_errorhandler(500)
def internal_server_error(e):
    """
    Internal Server Error error handler with HTTP content negotiation
    """
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify('error', 'internal app error')
        response.status_code = 500
        return response
    return render_template('500.html'), 500
