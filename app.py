#!bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/<var>')
def indexP(var):
    return "Hello, World! You've reached " + var

if __name__ == '__main__':
    app.run(debug = True)