from flask import Flask

app = Flask(__name__)

users = ['Alice', 'Bob', 'Charlie']

@app.route('/')
def index():
    return 'Index Page'
