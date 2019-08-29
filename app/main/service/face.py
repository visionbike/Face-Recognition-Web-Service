from datetime import datetime
from app.main.model import Face, Employee
from app.main.service import get_nfaces, increase_nfaces, decrease_nfaces, reset_nfaces, reset_all_nfaces
from app.main.util import insert, commit, delete
from app.main.util import code_200, code_201, code_400, code_404


def get_all_faces():
    return Face.query.all()


def delete_all_faces():
    # delete all faces
    faces = Face.query.all()
    if faces:
        delete(faces)
        # reset_all_nfaces()
    return code_200('Success to delete face database.')


def get_faces(staff_id):
    return Face.query.get(staff_id)


def delete_faces(staff_id):
    faces = Face.query.get(staff_id)
    if not faces:
        response = code_404('Not found faces with staff_id=\'{}\''.format(staff_id))
    else:
        delete(faces)
        # reset_nfaces(staff_id)
        response = code_200('Success to delete all faces with staff_id=\'{}\''.format(staff_id))
    return response


def add_face(data):
    employee = Employee.query.filter_by(id=data['staff_id']).first()
    if not employee:
        response = code_404('Not found employee with staff_id=\'{}\' in database'.format(data['staff_id']))
    else:
        new_face = Face(staff_id=data['staff_id'], name=data['name'])
        # insert face
        insert(new_face)
        # update num images
        # increase_nfaces(data['staff_id'])
        response = code_201('Success to add new face with staff_id=\'{}\''.format(data['staff_id']))
    return response


def update_face(data):
    face = Face.query.filter_by(image_id=data['image_id']).first()
    if not face:
        response = code_404('Not found face with id=\'{}\''.format(data['image_id']))
    else:
        for k in data.keys():
            if k == 'id':
                continue
            setattr(face, k, data[k])
        face.updated_on = datetime.utcnow()
        commit()
        response = code_200('Success to update face with id=\'{}\''.format(data['image_id']))
    return response


def delete_face(image_id):
    face = Face.query.get(image_id=image_id)
    if not face:
        response = code_404('Not found face with id=\'{}\''.format(image_id))
    else:
        delete(face)
        response = code_200('Success to delete all faces with id=\'{}\''.format(image_id))
    return response


def get_image(image_id):
    face = Face.query.filter_by(image_id=image_id).first()
    if not face:
        return None
    return face['name']







