import os
import time
from flask import Flask, Response, json, request
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)

db = os.path.join(os.getcwd(), 'database.db')


class Database(object):
    def __init__(self):
        self.connect = sqlite3.connect(db, check_same_thread=False)

    def querry(self, q, arg=()):
        cursor = self.connect.cursor()
        cursor.execute(q, arg)
        results = cursor.fetchall()
        cursor.close()
        return results

    def insert(self, q, arg=()):
        cursor = self.connect.cursor()
        cursor.execute(q, arg)
        self.connect.commit()
        result = cursor.lastrowid
        cursor.close()
        return result


app.config['file_allowed'] = ['image/png', 'image/jpeg']
app.config['storage'] = os.path.join(os.getcwd(), 'storage')
app.db = Database()


def success_handle(output, status=200, mimetype='aplication/json'):
    return Response(output, status=status, mimetype=mimetype)


def error_handle(error_message, status=500, mimetype='application/json'):
    return Response(json.dumps({'error': {'message': error_message}}), status=status, mimetype=mimetype)


@app.route('/', methods=['GET'])
def homepage():
    output = json.dumps({'api': '1.0'})
    return success_handle(output)


@app.route('/api/train', methods=['POST'])
def train():
    if 'image' not in request.files:
        print('Face image is required')
        return error_handle('Face image is required')
    else:
        print('image', request.files)
        image = request.files['image']
        if image.mimetype not in app.config['file_allowed']:
            print('File extension is not allowed')
            return error_handle('File extension is not allowed')
        else:
            # Get name in form data
            name = request.form['name']
            print('Information of the face:', name)
            print('File is allowed and will be save in ', app.config['storage'])
            # Save file
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['storage'], filename))
            print('New file name is', filename)
            # Save to sqlite data
            created = int(time.time())
            user_id = app.db.insert("INSERT INTO users(name, created) values(?,?)", [name, created])
            if user_id:
                print('User saved in data', name, user_id)
                face_id = app.db.insert('INSERT INTO faces(user_id, filename, created) values(?,?,?)', [user_id, filename, created])
                if face_id:
                    print('face hase been saved')
                    face_data = {'id': face_id, 'filename': filename, 'created': created}
                    output = json.dumps({'id': user_id, 'name': name, 'face_id': face_id, 'face': [face_data]})
                    return success_handle(output)
                else:
                    print('Error to save face image')
                    return error_handle('Error to save face image')

        print('Request contains image')
    output = json.dumps({'success': True})
    return success_handle(output)


if __name__ == '__main__':
    app.run(debug=True)
