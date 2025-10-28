from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# --- HTML Template with simple design (Bootstrap included) ---
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask API - Student Info</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #4A00E0, #8E2DE2);
            color: white;
            font-family: 'Poppins', sans-serif;
            text-align: center;
            padding-top: 5%;
        }
        .card {
            background-color: rgba(255,255,255,0.1);
            border: none;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        a.btn {
            background-color: #FFD700;
            border: none;
            color: #333;
            font-weight: bold;
        }
        a.btn:hover {
            background-color: #FFC300;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card mx-auto" style="max-width: 500px;">
            <h1>🎓 Welcome to My Flask API</h1>
            <p>This API provides information about a student.</p>
            <a href="/student" class="btn btn-lg">View Student Data</a>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/student', methods=['GET'])
def get_student():
    student_data = {
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    }
    return jsonify(student_data)

if __name__ == '__main__':
    app.run(debug=True)
