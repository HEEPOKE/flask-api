from flask import Flask
from config import config

app = Flask(__name__)

app.config.update(config)

users = ['Alice', 'Bob', 'Charlie']

@app.route('/')
def index():
    return config['DATABASE_URL']

app.run()
