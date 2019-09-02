from datetime import datetime
from marshmallow import fields
from .. import db, ma


class User(db.Model):
    """User model to store user related details"""
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, unique=True)
    fullname = db.Column(db.String(256), nullable=False)
    dept = db.Column(db.String(256), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    faces = db.relationship('Face', backref='user', cascade='all, delete, delete-orphan', single_parent=True, lazy='dynamic', order_by='desc(Note.user_id')

    def __repr__(self):
        return "<User '{}' - {}>".format(self.id, self.name)


class UserSchema(ma.ModelSchema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    class Meta:
        model = User
        sql_session = db.session

    faces = fields.Nested('UserFaceSchema', default=[], many=True)
