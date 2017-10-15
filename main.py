
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/baesic/<username>')
def yo(username):
    return 'My username is ' + username
