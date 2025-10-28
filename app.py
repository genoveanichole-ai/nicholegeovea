from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage for students
students = []

# ---------- HOME PAGE ----------
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Info Portal 🚀</title>
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
      font-size: 18px;
    }
    .btn-add { background: linear-gradient(90deg, #FFD700, #FFA500); }
    .btn-view { background: linear-gradient(90deg, #00C9FF, #92FE9D); }
    .btn-custom:hover { transform: scale(1.1); }
  </style>
</head>
<body>
  <div>
    <h1>💫 Welcome to <span style="color:#FFD700;">Student Info Portal</span></h1>
    <p>Manage your students easily with style! 🌟</p>
    <a href="/add_student" class="btn btn-custom btn-add">➕ Add Student</a>
    <a href="/view_students" class="btn btn-custom btn-view">👀 View Students</a>
  </div>
</body>
</html>
"""

# ---------- ADD STUDENT PAGE ----------
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
      border-radius: 20px;
      padding: 40px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.3);
      backdrop-filter: blur(15px);
      width: 100%;
      max-width: 500px;
      transition: 0.3s;
    }
    .form-card:hover { transform: scale(1.02); }
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
      font-size: 16px;
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

# ---------- VIEW STUDENTS PAGE (CARD DESIGN) ----------
view_students_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Info 👀</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: linear-gradient(135deg, #11998e, #38ef7d);
      font-family: 'Poppins', sans-serif;
      padding: 30px;
      min-height: 100vh;
    }
    .card-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 25px;
    }
    .student-card {
      background: rgba(255,255,255,0.15);
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 8px 30px rgba(0,0,0,0.3);
      backdrop-filter: blur(10px);
      transition: 0.3s;
    }
    .student-card:hover { transform: scale(1.03); }
    h5 { color: #FFD700; }
    p { color: #fff; margin: 5px 0; }
    .btn-delete {
      background: #FF4C4C;
      border: none;
      border-radius: 50px;
      padding: 5px 15px;
      color: white;
      font-weight: bold;
      transition: 0.2s;
      margin-top: 10px;
    }
    .btn-delete:hover { background: #FF0000; transform: scale(1.05); }
    .top-buttons {
      margin-bottom: 20px;
      text-align: center;
    }
    .btn-top {
      border-radius: 50px;
      padding: 10px 20px;
      font-weight: bold;
      margin: 5px;
      transition: 0.3s;
    }
    .btn-top:hover { transform: scale(1.05); }
  </style>
</head>
<body>
  <div class="top-buttons">
    <a href="/add_student" class="btn btn-warning btn-top">➕ Add Another</a>
    <a href="/" class="btn btn-dark btn-top">← Back to Portal</a>
  </div>
  {% if students %}
  <div class="card-container">
    {% for s in students %}
    <div class="student-card">
      <h5>{{ s.name }}</h5>
      <p><strong>ID:</strong> {{ s.student_id }}</p>
      <p><strong>Grade:</strong> {{ s.grade }}</p>
      <p><strong>Section:</strong> {{ s.section }}</p>
      <p><strong>Course:</strong> {{ s.course }}</p>
      <p><strong>Email:</strong> {{ s.email }}</p>
      <p><strong>Address:</strong> {{ s.address }}</p>
      <a href="/delete_student/{{ loop.index0 }}" class="btn btn-delete w-100">Delete</a>
    </div>
    {% endfor %}
  </div>
  {% else %}
  <p class="text-center mt-5" style="color:white; font-size:18px;">📭 No students added yet.</p>
  {% endif %}
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
