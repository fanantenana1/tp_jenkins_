#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello %s!\n' % username

@app.route('/feature/<name>')
def feature_route(name):
    return f'Feature test OK for {name}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
