from flask_restplus import fields, Namespace


class TrainDto(Namespace):
    api = Namespace('Train', description='Train related operations')
