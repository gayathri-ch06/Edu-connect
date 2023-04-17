import json
import csv
import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import text
from flask_socketio import *



app = Flask(__name__)
socketio = SocketIO(app, async_handlers=False)


file_path = os.path.abspath(os.getcwd()) + "\\e-connect.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/login/<string:userType>', methods=['POST'])
def login(userType):
    data = json.loads(request.data)
    email = data['email']
    password = data['password']

    if userType == 'student':

        sql = text('SELECT * FROM Students WHERE email = :email and password = :password')
        result = db.session.execute(sql, {'email': email, 'password': password})
        student_auth = [row[0] for row in result]

        if len(student_auth) > 0:
            print("Authentication Successful")
            return jsonify({'status': True, 'message': "Login Successful"})

        else:
            print("Authentication Failed")
            return jsonify({'status': False, 'error': "Invalid Credentials"})

    if userType == 'lecturer':

        sql = text('SELECT * FROM Professor WHERE email = :email and password = :password')
        result = db.session.execute(sql, {'email': email, 'password': password})
        lecturer_auth = [row[0] for row in result]

        if len(lecturer_auth) > 0:
            return jsonify({'status': True, 'message': "Login Successful"})

        else:
            return jsonify({'status': False, 'error': "Invalid Credentials"})


@app.route('/enrollCourse/<string:courseName>', methods=['POST'])
def enrollCourse(courseName):
    print("courseName", courseName)

    with open('files/courses.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == courseName:
                return jsonify({'status': True, 'message': "Already Enrolled"})
    with open('files/courses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([courseName])

    return jsonify({'status': True, 'message': "Enroll Successful"})


@app.route('/submit/<string:pageName>', methods=['POST'])
def submit(pageName):
    data = json.loads(request.data)
    print("courseName", data)
    if pageName == 'quiz':
        for i in data:
            question = i['question']
            answer = i['answer']
            with open('files/quiz.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([question, answer])

    if pageName == 'feedback':
        question = data['email']
        answer = data['feedback']
        with open('files/feedback.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([question, answer])

    return jsonify({'status': True, 'message': "Submission Successful"})


@app.route('/getData/<string:pageName>')
def get(pageName):
    data = []
    if pageName == 'students':
        with open('files/students.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append({'name': row[0]})

    if pageName == 'assignment':
        with open('files/assignment.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row)
                data.append({'question': row[0], 'data': row[1]})

    if pageName == 'quiz':
        with open('uploads/lecturer/Quiz/quiz.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row)
                data.append({'question': row[0], 'options': [row[1], row[2], row[3], row[4]], 'answer': row[5]})

    if pageName == 'feedback':
        with open('files/feedback.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                data.append({'email': row[0], 'feedback': row[1]})
    return jsonify({'message': data})


@app.route('/upload/<string:user>', methods=['POST'])
def upload_file(user):
    type = request.args.get('filetype')

    if 'file' not in request.files:
        return jsonify({'error': 'No file in request'})
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No filename'})

    filename = file.filename
    file_exists = os.path.exists('uploads/' + user + '/' + type)
    if file_exists:
        file.save(os.path.join('uploads/' + user + '/' + type, filename))
    else:
        os.makedirs('uploads/' + user + '/' + type)
        file.save(os.path.join('uploads/' + user + '/' + type, filename))

    return jsonify({'success': True, 'filename': filename})


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=8000)
