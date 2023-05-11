from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'FLASK_APP': os.environ.get('FLASK_APP', 'app.py'),
    'DATABASE_URL': os.environ.get('DATABASE_URL', 'postgresql://yoyo:5555@localhost/flask'),
    'PORT': str(os.environ.get('PORT', 6476)),
    'SECRET_KEY': os.environ.get('SECRET_KEY', 'my_secret_key'),
}
