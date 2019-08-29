from functools import wraps
from flask_restplus import marshal_with


def selective_marshal_with(fields):
    """
    Selective response marshalling. Doesn't update apidoc.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            model = fields
            func2 = marshal_with(model)(func)
            return func2(*args, **kwargs)
        return wrapper
    return decorator
