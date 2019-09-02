from app.main import db


def insert(data):
    db.session.add(data)
    db.session.commit()


def merge(data):
    db.session.merge(data)
    db.session.commit()


def delete(data):
    db.session.delete(data)
    db.session.commit()

