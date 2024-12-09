from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    headers = request.headers
    with open('log.txt', 'a') as file:
        file.write(f"IP Address: {ip}\n")
        file.write(f"Headers: {headers}\n")
    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Honeypot</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .container { max-width: 600px; margin: 0 auto; padding: 20px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the Honeypot</h1>
            <p>Your IP address and Device-type have been logged, Go Fuck Yourself.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
