from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from functools import wraps

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' not in session or session.get('role') != 'admin':
            return redirect('/dashboard')
        return f(*args, **kwargs)
    return wrapper

app = Flask(__name__)
app.secret_key = "a8f7sd9f87sd9f87sd9f87sdf"


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db = get_db()

    # auth table
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # student table
    db.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')

    db.commit() 

#get
@app.route('/')
def home():
    return redirect('/login')

from flask import jsonify

@app.route('/api/students', methods=['GET'])
def api_get_students():
    db = get_db()
    students = db.execute("SELECT * FROM students").fetchall()

    return jsonify([dict(row) for row in students])

#post
@app.route('/api/students', methods=['POST'])
def api_add_student():   
    if session.get('role') != 'admin':
        return jsonify({"error": "Admin only"}), 403
    data = request.get_json()

    db = get_db()
    db.execute(
        "INSERT INTO students (name, email) VALUES (?, ?)",
        (data['name'], data['email'])
    )
    db.commit()

    return jsonify({"message": "Student added"})

#put
@app.route('/api/students/<int:id>', methods=['PUT'])
def api_update_student(id):
    if session.get('role') != 'admin':
        return jsonify({"error": "Admin only"}), 403
    data = request.get_json()

    db = get_db()
    db.execute(
        "UPDATE students SET name=?, email=? WHERE id=?",
        (data['name'], data['email'], id)
    )
    db.commit()

    return jsonify({"message": "Updated"})

#delete
@app.route('/api/students/<int:id>', methods=['DELETE'])
def api_delete_student(id):
    if session.get('role') != 'admin':
        return jsonify({"error": "Admin only"}), 403
    db = get_db()
    db.execute("DELETE FROM students WHERE id=?", (id,))
    db.commit()

    return jsonify({"message": "Deleted"})


# ---------------- AUTH ---------------- #

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, password, 'user')   # default role
            )
            db.commit()
            return redirect('/login')

        except:
            error = "Username already exists ❌"

    return render_template('register.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()

        if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            session['role'] = user['role']
            return redirect('/dashboard')
        else:
            error = "Invalid username or password ❌"

    return render_template('login.html', error=error)

@app.route('/admin')
@admin_required
def admin_dashboard():
    db = get_db()
    users = db.execute("SELECT id, username, role FROM users").fetchall()

    return render_template('admin.html', users=users)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# ---------------- DASHBOARD ---------------- #

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    total_students = db.execute("SELECT COUNT(*) FROM students").fetchone()[0]

    return render_template('dashboard.html', user=session['user'], total_students=total_students)


# ---------------- CRUD ---------------- #

@app.route('/students')
def students():
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    students = db.execute("SELECT * FROM students").fetchall()

    return render_template('students.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
@admin_required
def add_student():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        db = get_db()
        db.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        db.commit()

        return redirect('/students')

    return render_template('add_student.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_student(id):
    if 'user' not in session:
        return redirect('/login')

    db = get_db()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        db.execute("UPDATE students SET name=?, email=? WHERE id=?", (name, email, id))
        db.commit()

        return redirect('/students')

    student = db.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()

    return render_template('edit_student.html', student=student)


@app.route('/delete/<int:id>')
@admin_required
def delete_student(id):
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    db.execute("DELETE FROM students WHERE id=?", (id,))
    db.commit()

    return redirect('/students')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)