from flask import Flask, request
import logging
from datetime import datetime

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    filename="honeypot_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

@app.route("/", methods=["GET", "POST"])
def fake_login():
    if request.method == "POST":
        # Capture login attempt details
        attacker_ip = request.remote_addr
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Log the attempt
        log_message = f"Login attempt from {attacker_ip} | Username: {username} | Password: {password}"
        logging.info(log_message)
        print(log_message)  # For real-time feedback

        # Respond with a fake error
        return "Invalid username or password", 401

    # Render the fake login page
    return """
    <html>
    <head><title>Login</title></head>
    <body>
        <h1>Login Page</h1>
        <form method="POST" action="/">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
