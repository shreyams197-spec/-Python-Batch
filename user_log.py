
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Login credentials
INBUILT_USER_NAME = "admin"
INBUILT_USER_PASSWORD = "admin123"

# HTML + CSS + Flask in one file
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #10172f, #45318a, #8c5cf6);
            padding: 20px;
        }

        .login-container {
            width: 100%;
            max-width: 400px;
            padding: 40px 32px;
            border-radius: 22px;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.25);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(15px);
            color: white;
        }

        .logo {
            width: 65px;
            height: 65px;
            margin: 0 auto 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 18px;
            background: #a78bfa;
            color: #201044;
            font-size: 30px;
            font-weight: bold;
        }

        h1 {
            text-align: center;
            font-size: 30px;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            color: #ddd6fe;
            font-size: 14px;
            margin-bottom: 30px;
        }

        label {
            display: block;
            margin-bottom: 9px;
            font-size: 14px;
            font-weight: bold;
        }

        input {
            width: 100%;
            padding: 14px;
            margin-bottom: 22px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            font-size: 15px;
            outline: none;
        }

        input::placeholder {
            color: #d1cbe7;
        }

        input:focus {
            border-color: #c4b5fd;
            box-shadow: 0 0 0 3px rgba(196, 181, 253, 0.15);
        }

        button {
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(90deg, #c4b5fd, #a78bfa);
            color: #211342;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(167, 139, 250, 0.3);
        }

        .message {
            margin-top: 20px;
            padding: 12px;
            border-radius: 9px;
            text-align: center;
            font-size: 14px;
        }

        .success {
            background: rgba(34, 197, 94, 0.2);
            color: #bbf7d0;
            border: 1px solid #4ade80;
        }

        .error {
            background: rgba(239, 68, 68, 0.2);
            color: #fecaca;
            border: 1px solid #f87171;
        }

        .footer {
            text-align: center;
            margin-top: 25px;
            color: #ddd6fe;
            font-size: 12px;
        }

        @media (max-width: 480px) {
            .login-container {
                padding: 32px 22px;
            }

            h1 {
                font-size: 26px;
            }
        }
    </style>
</head>

<body>
    <div class="login-container">

        <div class="logo">S</div>

        <h1>Welcome Back</h1>
        <p class="subtitle">Sign in to continue to your account</p>

        <form method="POST">
            <label for="user_name">Username</label>
            <input
                type="text"
                id="user_name"
                name="user_name"
                placeholder="Enter your username"
                required
            >

            <label for="user_password">Password</label>
            <input
                type="password"
                id="user_password"
                name="user_password"
                placeholder="Enter your password"
                required
            >

            <button type="submit">Sign In</button>
        </form>

        {% if message %}
            <div class="message {{ status }}">
                {{ message }}
            </div>
        {% endif %}

        <p class="footer">Secure Login Portal</p>

    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    status = ""

    if request.method == "POST":
        user_name = request.form.get("user_name", "")
        user_password = request.form.get("user_password", "")

        if (user_name == INBUILT_USER_NAME
                and user_password == INBUILT_USER_PASSWORD):
            message = "Login successful! Welcome, admin."
            status = "success"
        else:
            message = "Invalid username or password."
            status = "error"

    return render_template_string(
        HTML_PAGE,
        message=message,
        status=status
    )


if __name__ == "__main__":
    app.run(debug=True)
