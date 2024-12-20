from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission, process data if necessary
        email = request.form.get('email')
        # You can log the email or perform other tasks here
        print(f"Email: {email}")

        # Redirect to password page after form submission
        return redirect(url_for('password'))  # This will redirect to the /password route

    return render_template('index.html')

@app.route('/password')
def password():
    # Render the password.html page
    return render_template('password.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
