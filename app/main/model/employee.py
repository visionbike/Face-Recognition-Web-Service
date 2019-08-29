from datetime import datetime
from .. import db


class Employee(db.Model):
    """Employee model to store employee related details"""
    __tablename__ = 'employee'

    id = db.Column(db.String(32), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    dept = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    nimages = db.Column(db.Integer(), nullable=False, default=0)
    created_on = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())
    faces = db.relationship('Face', backref='employee', lazy='dynamic')

    def __repr__(self):
        return "<Employee '{}' - {}>".format(self.id, self.name)
