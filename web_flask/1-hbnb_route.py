#!/usr/bin/python3
""" Import flask class """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """ Function to handle request """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """ Function to handle request to path /hbnb """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
