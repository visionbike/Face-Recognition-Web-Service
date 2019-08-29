# from flasgger import Swagger
from flask import Flask
from flask_bcrypt import Bcrypt
# from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .config import config

db = SQLAlchemy()
bcrypt = Bcrypt()
# api = Api(prefix='/api')

# swagger_config = {'headers': [('Access-Control-Allow-Origin', '*'),
#                               ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE'),
#                               ('Access-Control-Allow-Credentials', 'true')],
#                   'specs': [{'endpoint': 'docs',
#                              'route': '/docs.json',
#                              'rule_filter': lambda rule: True,  # all in
#                              'model_filter': lambda tag: True,  # all in
#                              }],
#                   'static_url_path': '/flasgger_static',
#                   'specs_route': '/docs/',
#                   'uiversion': 3}
#
# swagger_template = {'swagger': '2.0',
#                     'info': {'title': 'Lac Viet Face Recognition API',
#                              'description': '',
#                              'contact': {'responsibleOrganization': 'Lac Viet Computing Corp.',
#                                          'responsibleDeveloper': '',
#                                          'email': '',
#                                          'url': ''},
#                              'termsOfService': '',
#                              'version': '1.0.0'},
#                     # 'basePath': '/api',
#                     'schemes': ['http', 'https'],
#                     'produces': ['application/json']}
#
# swagger = Swagger(config=swagger_config, template=swagger_template)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    bcrypt.init_app(app)
    # api.init_app(app)
    # swagger.init_app(app)

    return app