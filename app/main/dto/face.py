from flask_restplus import fields, Namespace


class FaceDto(Namespace):
    api = Namespace('Face', description='Face image related operations')
    face = api.model('Face', {'image_id': fields.Integer(description='identifier'),
                              'staff_id': fields.String(description='staff identifier'),
                              'name': fields.String(description='face filename'),
                              'created_on': fields.DateTime(description='created time'),
                              'updated_on': fields.DateTime(description='updated time')})
