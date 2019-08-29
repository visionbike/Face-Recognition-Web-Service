from flask import request
from flask_restplus import Resource
from werkzeug import datastructures
from werkzeug.utils import secure_filename
from ..service import get_all_faces, delete_all_faces, get_faces, delete_faces, add_face, update_face, delete_face, get_image
from ..util import save_image, delete_image, delete_images
from ..dto import FaceDto
from ..config import BaseConfig

api = FaceDto.api
_face = FaceDto.face

post_upload_parser = api.parser()
post_upload_parser.add_argument('image', location='files', type=datastructures.FileStorage, required=True, help='Face image')


@api.route('/')
class FaceList(Resource):
    @api.doc('Get faces from staff')
    @api.marshal_list_with(_face, envelope='data')
    def get(self):
        """
        Get faces from staff
        """
        return get_all_faces()

    @api.doc('Delete face database')
    @api.response(200, 'Success to delete face database.')
    def delete(self):
        """
        Delete face database
        """
        return delete_all_faces()


@api.route('/by_image_id/<int:image_id>')
@api.param('image_id', 'Image identifier', _in='query')
class Face(Resource):
    @api.doc('Update face')
    @api.response(201, 'Success to update new face from id.')
    @api.response(400, 'Fail to update new faces.')
    @api.response(404, 'Not found face.')
    @api.response(405, 'The method not allowed.')
    @api.param('staff_id', 'Employee identifier', _in='formData')
    @api.expect(post_upload_parser, validate=True)
    def put(self, staff_id, image_id):
        """
        Update employee's face given id
        """
        if 'image' not in request.files:
            return api.abort(405, error='method not allowed', message='Request must contain `image`.')

        im = request.files['image']
        if im.mimetype not in BaseConfig.FILE_ALLOWED:
            return api.abort(405, error='method not allowed', message='File extension is not allowed.')

        if not delete_image(BaseConfig.STORAGE, get_image(image_id)):
            return api.abort(400, error='bad request',
                             message='Fail to update face with id=\'{}\''.format(staff_id))
        # _, ext = os.path.splitext(im.filename)
        filename = secure_filename('{}.{}'.format(staff_id, im.filename))
        if not save_image(BaseConfig.STORAGE, filename, im):
            return api.abort(400, error='bad request',
                             message='Fail to update new face with id=\'{}\''.format(staff_id))

        data = {'staff_id': staff_id, 'id': image_id, 'name': filename}
        return update_face(data)

    @api.doc('Delete face given id')
    @api.response(201, 'Success to delete face from id.')
    @api.response(400, 'Fail to delete face.')
    @api.response(404, 'Not found face.')
    @api.response(405, 'The method not allowed.')
    def delete(self, image_id):
        """
        Delete employee's face given id
        """
        if not delete_image(BaseConfig.STORAGE, get_image(image_id)):
            return api.abort(400, error='bad request',
                             message='Fail to delete face with id=\'{}\''.format(image_id))
        return delete_face(image_id)


@api.route('/by_staff_id/<string:staff_id>')
@api.param('staff_id', 'Employee identifier', _in='query')
class StaffFace(Resource):
    @api.doc('Get all faces from employee id')
    @api.response(200, 'Success to get faces.')
    @api.response(404, 'Not found faces.')
    @api.marshal_list_with(_face, envelope='data')
    def get(self, staff_id):
        """
        Get all faces from employee id
        """
        faces = get_faces(staff_id)
        if not faces:
            return api.abort(404, error='not found', message='Not found faces of employee with staff_id=\'{}\''.format(staff_id))
        return faces

    @api.doc('Add new face from employee id')
    @api.response(201, 'Success to add new face from employee id.')
    @api.response(400, 'Fail to add new faces.')
    @api.response(404, 'Not found employee.')
    @api.response(405, 'The method not allowed.')
    @api.expect(post_upload_parser, validate=True)
    def post(self, staff_id):
        """
        Create new employee's face
        """
        if 'image' not in request.files:
            return api.abort(405, error='method not allowed', message='Request must contain `image`.')

        im = request.files['image']
        if im.mimetype not in BaseConfig.FILE_ALLOWED:
            return api.abort(405, error='method not allowed', message='File extension is not allowed.')

        # _, ext = os.path.splitext(im.filename)
        filename = secure_filename('{}.{}'.format(staff_id, im.filename))
        if not save_image(BaseConfig.STORAGE, filename, im):
            return api.abort(400, error='bad request',
                             message='Fail to add new face with staff_id=\'{}\''.format(staff_id))
        data = {'staff_id': staff_id, 'name': filename}
        return add_face(data)

    @api.doc('Delete all faces from employee id')
    @api.response(200, 'Success to delete all faces from employee id.')
    @api.response(400, 'Fail to delete faces.')
    @api.response(404, 'Not found faces.')
    def delete(self, staff_id):
        """
        Delete a face image given its employee identifier
        """
        if not delete_images(BaseConfig.STORAGE, staff_id):
            return api.abort(400, error='bad request', message='Fail to delete faces with staff_id=\'{}\''.format(staff_id))
        return delete_faces(staff_id)
