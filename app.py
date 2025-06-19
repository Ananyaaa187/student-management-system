# Enhanced Student Management System (with name, email, USN, year) using Flask + JSON

from flask import Flask, render_template, request, redirect, url_for, session
import os
import json

app = Flask(__name__)
app.secret_key = 'secret123'

DATA_FILE = 'students.json'

# Load student data
def load_students():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save student data
def save_students(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        roll = request.form['roll']
        year = request.form['year']
        password = request.form['password']

        students = load_students()
        if roll in students:
            return 'Student already registered!'

        students[roll] = {
            'name': name,
            'email': email,
            'roll': roll,
            'year': year,
            'password': password,
            'attendance': {},
            'marks': {}
        }
        save_students(students)
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        roll = request.form['roll']
        password = request.form['password']

        students = load_students()
        student = students.get(roll)

        if student and student['password'] == password:
            session['roll'] = roll
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials!'

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'roll' not in session:
        return redirect(url_for('login'))

    roll = session['roll']
    students = load_students()
    student = students.get(roll)
    return render_template('dashboard.html', student=student)

@app.route('/logout')
def logout():
    session.pop('roll', None)
    return redirect(url_for('home'))

@app.route('/update_attendance', methods=['POST'])
def update_attendance():
    roll = request.form['roll']
    subject = request.form['subject']
    count = int(request.form['count'])

    students = load_students()
    if roll in students:
        students[roll]['attendance'][subject] = count
        save_students(students)
    return redirect(url_for('dashboard'))

@app.route('/update_marks', methods=['POST'])
def update_marks():
    roll = request.form['roll']
    subject = request.form['subject']
    mark = int(request.form['mark'])

    students = load_students()
    if roll in students:
        students[roll]['marks'][subject] = mark
        save_students(students)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)