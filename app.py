from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

# --- HTML Template with modern, glass-style design ---
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cool Student API 🌐</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #6a11cb, #2575fc);
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
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
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
        .btn-custom {
            background: linear-gradient(90deg, #FFD700, #FFA500);
            color: #222;
            font-weight: 600;
            border: none;
            border-radius: 50px;
            padding: 12px 25px;
            transition: 0.3s;
        }
        .btn-custom:hover {
            background: linear-gradient(90deg, #FFB700, #FF8C00);
            color: white;
        }
        .result-box {
            margin-top: 20px;
            display: none;
            background-color: rgba(0,0,0,0.3);
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            font-size: 2rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card mx-auto" style="max-width: 500px;">
            <h1>🎓 Student Info API</h1>
            <p>Click below to fetch data from the Flask API!</p>
            <button id="fetchBtn" class="btn btn-custom">Get Student Data</button>
            <div id="result" class="result-box">
                <h4>📘 API Result:</h4>
                <pre id="jsonData" style="color: #FFD700; font-weight: 500;"></pre>
            </div>
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

@app.route('/student', methods=['GET'])
def get_student():
    student_data = {
        "name": "John Zechariah",
        "grade": 10,
        "section": "Alpha",
        "hobby": "Coding & Basketball 🏀",
        "quote": "Code the future, one line at a time 💻"
    }
    return jsonify(student_data)

if __name__ == '__main__':
    app.run(debug=True)
