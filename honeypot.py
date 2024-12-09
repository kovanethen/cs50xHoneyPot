from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Log request details
    ip = request.remote_addr
    headers = request.headers
    print(f"IP Address: {ip}")
    print(f"Headers: {headers}")
    return 'Hello, Honeypot!'

if __name__ == '__main__':
    app.run(debug=True)
    
with open('log.txt', 'a') as file:
    file.write(f"IP Address: {ip}\n")
    file.write(f"Headers: {headers}\n")