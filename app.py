from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# ---------- PAGE 1: WELCOME ----------
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
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
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
        .fade-in {
            animation: fadeIn 3s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container fade-in">
        <h1>💫 Welcome to <span style="color:#FFD700;">KUKA API</span></h1>
        <p class="lead mt-3">Explore the magic of data with style and power.</p>
        <a href="/dashboard" class="btn btn-enter">Enter App 🚪</a>
    </div>
</body>
</html>
"""

# ---------- PAGE 2: DASHBOARD ----------
dashboard_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KUKA Student Dashboard 🎓</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #1f1c2c, #928DAB);
            color: white;
            font-family: 'Poppins', sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: rgba(255,255,255,0.15);
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(31,38,135,0.37);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.18);
            padding: 40px;
            text-align: center;
            transition: all 0.3s ease;
        }
        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        }
        .btn-fetch {
            background: linear-gradient(90deg, #FF512F, #DD2476);
            border: none;
            color: white;
            font-weight: 600;
            border-radius: 50px;
            padding: 12px 25px;
            transition: 0.3s;
        }
        .btn-fetch:hover {
            background: linear-gradient(90deg, #DD2476, #FF512F);
            transform: scale(1.05);
        }
        .result-box {
            margin-top: 25px;
            display: none;
            background-color: rgba(0,0,0,0.4);
            padding: 20px;
            border-radius: 10px;
        }
        pre {
            color: #00FFAA;
            font-weight: 600;
        }
        .btn-back {
            margin-top: 20px;
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
    </style>
</head>
<body>
    <div class="container">
        <div class="card mx-auto" style="max-width: 500px;">
            <h1>🎓 Student Info</h1>
            <p>Click below to get data from your Flask API.</p>
            <button id="fetchBtn" class="btn btn-fetch">Fetch Student Data ⚡</button>

            <div id="result" class="result-box">
                <h5>📘 API Response:</h5>
                <pre id="jsonData"></pre>
            </div>

            <a href="/" class="btn-back">← Back to Home</a>
        </div>
    </div>

    <script>
        document.getElementById('fetchBtn').addEventListener('click', async () => {
            const response = await fetch('/student');
            const data = await response.json();
            document.getElementById('jsonData').textContent = JSON.stringify(data, null, 2);
            document.getElementById('result').style.display = 'block';
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/dashboard')
def dashboard():
    return render_template_string(dashboard_html)

@app.route('/student')
def student():
    student_data = {
        "name": "Kuka Zechariah",
        "grade": 10,
        "section": "Alpha",
        "hobby": "Coding, Music 🎧, and Gaming 🎮",
        "favorite_quote": "Dream big, code bigger 💻",
        "api_version": "v2.0"
    }
    return jsonify(student_data)

if __name__ == '__main__':
    app.run(debug=True)
