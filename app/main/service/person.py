from datetime import datetime
from app.main import db
from app.main.model import Person, PersonSchema, Face
from app.main.util import insert, merge, delete
from app.main.util import code_200, code_201, code_404, code_409


def get_users():
    """
    Respond to a request for `/api/user` with the complete lists of people

    :return: json string of list of people
    """
    users = User.query.order_by(User.user_id).all()

    # Serialize the data for the response
    schema = UserSchema(many=True)
    data = schema.dump(users).data
    return data


def get_user(user_id):
    """
    Respond to a request for `/api/user/{user_id}` with one matching user from user id

    :param user_id: Id of user to find
    :return:        user data matching id if success
                    404 if not found
    """
    user = User.query.filter(User.user_id == user_id).outerjoin(Face).one_or_none()
    if not user:
        return code_404('Not found user with id={user_id}.')
    else:
        # Serialize the data for response
        schema = UserSchema()
        data = schema.dump(user).data
        return data


def create_user(user_data):
    """
    Create a new person in the user structure based on the passed in user data

    :param user_data: data to create in user structure
    :return:     201 if success
                 409 if user exists
    """
    user = User.query.filter(User.user_id == user_data.get('user_id')).one_or_none()
    if not user:
        schema = UserSchema()
        new_user = schema.load(user, session=db.session).data
        new_user.created_on = datetime.utcnow()

        # Add new user to database
        insert(new_user)

        response = code_201('Success to create new user with id={user_id}.')
    else:
        response = code_409('User with id={user_id} already exists.')
    return response


def update_user(user_id, user):
    """
    Update an existing user in the user structure

    :param user_id: Id of the user to update in the user structure
    :param user:    user data to update
    :return:        200 if success
                    404 if not found
    """
    user = User.query.filter(User.user_id == user_id).one_or_none()
    if not user:
        response = code_404('Not found user with id={user_id}.')
    else:
        schema = UserSchema()
        updating_user = schema.load(user, session=db.session).data

        # Set the id of the user and update date to update
        updating_user.user_id = user.user_id
        updating_user.updated_on = datetime.utcnow()

        # merge the new object into old
        merge(updating_user)

        response = code_200('Success to update user with id={user_id}.')
    return response


def delete_user(user_id):
    """
    Delete a user from the user structure

    :param user_id: Id of the user to delete
    :return:        200 if success
                    404 if not found
    """
    user = User.query.filter(User.user_id == user_id).one_or_none()
    if not user:
        response = code_404('Not found user with id={user_id}.')
    else:
        delete(user)
        response = code_200('Success to delete user with id={}.')
    return response
