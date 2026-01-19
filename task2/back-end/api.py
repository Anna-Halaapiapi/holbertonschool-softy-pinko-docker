# Uses Flask to create one endpoint that returns “Hello, World!” when called

from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Hosting Flask app on 0.0.0.0 instead of 127.0.0.1 - reachable outside of the current machine (a Docker container running inside your PC)
    app.run(host='0.0.0.0', port=5252)
