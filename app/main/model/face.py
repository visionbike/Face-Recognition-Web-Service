from datetime import datetime
from .. import db


class Face(db.Model):
    """Face model to store face related details"""
    __tablename__ = 'face'

    image_id = db.Column(db.Integer(), primary_key=True, unique=True, autoincrement=True, nullable=False)
    staff_id = db.Column(db.String(32), db.ForeignKey('employee.id'), nullable=False)
    # image_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(256), unique=True, nullable=False)
    created_on = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __repr__(self):
        return "<Face of Employee '{}' - {}>".format(self.staff_id, self.name)
