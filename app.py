from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def basic_route():
    # Get some user data
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    # Print the user data to record it with filebeat
    print(f"Client IP: {client_ip}")
    # return a string
    return 'Welcome'

if __name__ == '__main__':
    # Start the testapp
    app.run(host='0.0.0.0', port=8080)
