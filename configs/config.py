import os
from dotenv import load_dotenv

load_dotenv()

config_app = {
    'DEBUG': True,
    "FLASK_APP": os.environ.get("FLASK_APP", "app.py"),
    "DB_NAME": os.environ.get("DB_NAME", "flask"),
    "DB_PORT": os.environ.get("DB_PORT", "5432"),
    "DB_USERNAME": os.environ.get("DB_USERNAME", "yoyo"),
    "DB_PASSWORD": os.environ.get("DB_PASSWORD", "yoyo5555"),
    "DATABASE_URL": os.environ.get(
        "DATABASE_URL", "postgresql://yoyo:5555@localhost/flask"
    ),
    "PORT": str(os.environ.get("PORT", 6476)),
    "SECRET_KEY": os.environ.get("SECRET_KEY", "my_secret_key"),
}
