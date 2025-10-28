from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage for students
students = []

# ---------- PAGE 1: HOME ----------
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome to Student Data </title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
      color: white;
      font-family: 'Poppins', sans-serif;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
    }
    .btn-custom {
      margin: 15px;
      padding: 15px 35px;
      border-radius: 50px;
      font-weight: bold;
      border: none;
      transition: 0.3s;
      color: #222;
    }
    .btn-add { background: linear-gradient(90deg, #FFD700, #FFA500); }
    .btn-view { background: linear-gradient(90deg, #00C9FF, #92FE9D); }
    .btn-custom:hover { transform: scale(1.1); }
  </style>
</head>
<body>
  <div>
    <h1>💫 Welcome to <span style="color:#FFD700;">Student Info Portal</span></h1>
    <p>Manage your students easily.</p>
    <a href="/add_student" class="btn btn-custom btn-add">➕ Add Student</a>
    <a href="/view_students" class="btn btn-custom btn-view">👀 View Students</a>
  </div>
</body>
</html>
"""

# ---------- PAGE 2: ADD STUDENT ----------
add_student_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Add Student ✍️</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: white;
      font-family: 'Poppins', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
    .form-card {
      background: rgba(255,255,255,0.12);
      border-radius: 16px;
      padding: 40px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
      backdrop-filter: blur(10px);
      width: 100%;
      max-width: 500px;
    }
    .form-control {
      background: rgba(255,255,255,0.2);
      border: none;
      color: white;
    }
    .form-control::placeholder { color: #ddd; }
    .btn-submit {
      background: linear-gradient(90deg, #FF512F, #F09819);
      border: none;
      color: white;
      border-radius: 50px;
      padding: 10px 25px;
      font-weight: bold;
    }
    .btn-submit:hover { transform: scale(1.05); }
    a { color: #FFD700; text-decoration: none; }
  </style>
</head>
<body>
  <form action="/add_student" method="POST" class="form-card">
    <h2 class="text-center mb-4">📝 Add Student</h2>
    <div class="mb-3">
      <input type="text" class="form-control" name="student_id" placeholder="Student ID" required>
    </div>
    <div class="mb-3">
      <input type="text" class="form-control" name="name" placeholder="Full Name" required>
    </div>
    <div class="mb-3">
      <input type="text" class="form-control" name="grade" placeholder="Grade Level" required>
    </div>
    <div class="mb-3">
      <input type="text" class="form-control" name="section" placeholder="Section" required>
    </div>
    <div class="mb-3">
      <input type="text" class="form-control" name="course" placeholder="Course" required>
    </div>
    <div class="mb-3">
      <input type="email" class="form-control" name="email" placeholder="Email" required>
    </div>
    <div class="mb-3">
      <input type="text" class="form-control" name="address" placeholder="Address" required>
    </div>
    <button type="submit" class="btn btn-submit w-100">Add Student</button>
    <p class="text-center mt-3"><a href="/">← Back to Portal</a></p>
  </form>
</body>
</html>
"""

# ---------- PAGE 3: VIEW STUDENTS ----------
view_students_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>View Students 👀</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: linear-gradient(135deg, #11998e, #38ef7d);
      color: white;
      font-family: 'Poppins', sans-serif;
      padding: 40px;
    }
    table {
      background: rgba(255,255,255,0.15);
      border-radius: 10px;
      backdrop-filter: blur(8px);
    }
    th { color: #FFD700; }
    .btn-back {
      background-color: transparent;
      border: 2px solid #FFD700;
      color: #FFD700;
      border-radius: 50px;
      padding: 10px 25px;
      text-decoration: none;
      transition: 0.3s;
    }
    .btn-back:hover {
      background-color: #FFD700;
      color: #222;
    }
    .btn-delete {
      background: #FF4C4C;
      border: none;
      border-radius: 50px;
      padding: 5px 15px;
      color: white;
      font-weight: bold;
      transition: 0.2s;
    }
    .btn-delete:hover { background: #FF0000; transform: scale(1.05); }
  </style>
</head>
<body>
  <div class="container">
    <h2 class="text-center mb-4">👀 Student Info</h2>
    {% if students %}
    <table class="table table-striped table-bordered text-center align-middle">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Grade</th>
          <th>Section</th>
          <th>Course</th>
          <th>Email</th>
          <th>Address</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {% for s in students %}
        <tr>
          <td>{{ s.student_id }}</td>
          <td>{{ s.name }}</td>
          <td>{{ s.grade }}</td>
          <td>{{ s.section }}</td>
          <td>{{ s.course }}</td>
          <td>{{ s.email }}</td>
          <td>{{ s.address }}</td>
          <td>
            <a href="/delete_student/{{ loop.index0 }}" class="btn btn-delete">Delete</a>
          </td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
    {% else %}
    <p class="text-center mt-5">📭 No students added yet.</p>
    {% endif %}
    <div class="text-center mt-4">
      <a href="/add_student" class="btn btn-warning me-2">➕ Add Another</a>
      <a href="/" class="btn-back">← Back to Portal</a>
    </div>
  </div>
</body>
</html>
"""

# ---------- ROUTES ----------
@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student = {
            "student_id": request.form['student_id'],
            "name": request.form['name'],
            "grade": request.form['grade'],
            "section": request.form['section'],
            "course": request.form['course'],
            "email": request.form['email'],
            "address": request.form['address']
        }
        students.append(student)
        return redirect(url_for('view_students'))
    return render_template_string(add_student_html)

@app.route('/view_students')
def view_students():
    return render_template_string(view_students_html, students=students)

@app.route('/delete_student/<int:index>')
def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)
    return redirect(url_for('view_students'))

@app.route('/student_api')
def student_api():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
