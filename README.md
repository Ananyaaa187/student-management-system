
# Student Management System 🧑‍🎓

A simple web-based student management system built using Flask.
StudentManagementWebApp/
├── app.py
├── students.json        ← (optional: keep empty or exclude using .gitignore)
├── requirements.txt     ← (we’ll create this below)
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html

## Features
- Register & Login students
- View and update attendance
- View and update marks
- JSON-based storage (no database needed)

## How to Run
```bash
pip install -r requirements.txt
python app.py
    or
IN COMMAND PROMPT
cd "C:\Users\hp\Desktop\Student Management Web App"
python app.py
then you'll get
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 752-291-615
then open: http://127.0.0.1:5000
