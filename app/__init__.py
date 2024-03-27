import os

from flask import Flask
from dotenv import load_dotenv

# Загружаем окружные переменные
load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "secret string")

from app import views
