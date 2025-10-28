from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# ---------- PAGE 1: HOME / PORTAL ----------
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KUKA API Portal 🚀</title>
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
        h1 {
            font-size: 3rem;
            animation: glow 2s infinite alternate;
        }
        @keyframes glow {
            from { text-shadow: 0 0 10px #FFD700; }
            to { text-shadow: 0 0 25px #00FFFF; }
        }
        .btn-enter {
            margin-top: 30px;
            background: linear-gradient(90deg, #00C9FF, #92FE9D);
            border: none;
            color: #222;
            font-weight: bold;
            padding: 15px 40px;
            border-radius: 50px;
            transition: 0.4s;
            font-size: 1.1rem;
        }
        .btn-enter:hover {
            background: linear-gradient(90deg, #92FE9D, #00C9FF);
            transform: scale(1.1);
        }
        p {
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div>
        <h1>💫 Welcome to <span style="color:#FFD700;">KUKA API Portal</span></h1>
        <p>Access your student profile and data anytime, anywhere.</p>
        <a href="/student_data" class="btn btn-enter">Go to Student Data 🎓</a>
    </div>
</body>
</html>
"""

# ---------- PAGE 2: STUDENT DATA ----------
student_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KUKA Student Data 🎓</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-family: 'Poppins', sans-serif;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            padding: 30px;
        }
        .card {
            background: rgba(255,255,255,0.12);
            border-radius: 16px;
            padding: 40px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            backdrop-filter: blur(10px);
            text-align: left;
            max-width: 600px;
            width: 100%;
            transition: 0.4s;
        }
        .card:hover {
            transform: scale(1.03);
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #FFD700;
        }
        .info-label {
            font-weight: 600;
            color: #00FFAA;
        }
        .info-value {
            margin-bottom: 10px;
            font-size: 1.1rem;
        }
        .btn-back {
            margin-top: 25px;
            background-color: transparent;
            border: 2px solid #FFD700;
            color: #FFD700;
            border-radius: 50px;
            padding: 10px 25px;
            text-decoration: none;
            transition: 0.3s;
            display: inline-block;
        }
        .btn-back:hover {
            background-color: #FFD700;
            color: #222;
        }
        .btn-json {
            background: linear-gradient(90deg, #FF512F, #F09819);
            border: none;
            color: white;
            border-radius: 50px;
            padding: 10px 25px;
            margin-top: 15px;
            font-weight: 600;
            transition: 0.3s;
        }
        .btn-json:hover {
            background: linear-gradient(90deg, #F09819, #FF512F);
        }
        .json-box {
            background: rgba(0,0,0,0.4);
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            display: none;
            color: #00FFAA;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>🎓 Student Information</h2>
        <div class="info-value"><span class="info-label">Student ID:</span> 2025-001</div>
        <div class="info-value"><span class="info-label">Name:</span> Kuka Zechariah</div>
        <div class="info-value"><span class="info-label">Gender:</span> Male</div>
        <div class="info-value"><span class="info-label">Grade Level:</span> 10</div>
        <div class="info-value"><span class="info-label">Section:</span> Alpha</div>
        <div class="info-value"><span class="info-label">Course:</span> ICT - Programming</div>
        <div class="info-value"><span class="info-label">Email:</span> kuka.zechariah@studentportal.edu</div>
        <div class="info-value"><span class="info-label">Address:</span> Brgy. Malipayon, Iloilo City</div>
        <div class="info-value"><span class="info-label">Hobby:</span> Coding 💻, Gaming 🎮, Music 🎧</div>
        <div class="info-value"><span class="info-label">Quote:</span> "Dream big, code bigger." 🌟</div>

        <button id="show-json" class="btn btn-json">Show API JSON 📦</button>
        <pre id="json-box" class="json-box"></pre>

        <a href="/" class="btn-back">← Back to Portal</a>
    </div>

    <script>
        document.getElementById('show-json').addEventListener('click', async () => {
            const res = await fetch('/student_api');
            const data = await res.json();
            const pre = document.getElementById('json-box');
            pre.textContent = JSON.stringify(data, null, 2);
            pre.style.display = 'block';
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/student_data')
def student_data():
    return render_template_string(student_html)

@app.route('/student_api')
def student_api():
    student_data = {
        "student_id": 
        "name": 
        "gender":
        "grade_level": 
        "section": 
        "course": 
        "email": 
        "address": 
        "hobby": 
        "quote": 
    }
    return jsonify(student_data)

if __name__ == '__main__':
    app.run(debug=True)
