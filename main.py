from flask import Flask
from configs.config import config_app

app = Flask(__name__)

app.config.update(config_app)

users = ['Alice', 'Bob', 'Charlie']

@app.route('/')
def index():
    return app.config['DATABASE_URL']

if __name__ == '__main__':
    app.run()
