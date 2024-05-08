import os

from flask import Flask
from dotenv import load_dotenv
from flask import jsonify, make_response
from flask_login import LoginManager
from .blueprints import index, authentication, products
from app.database.repository import UserRepository

# Загружаем окружные переменные
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "secret string")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


app.register_blueprint(index.index)
app.register_blueprint(authentication.authentication)
app.register_blueprint(products.products, url_prefix='/products')

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id: int):
    return UserRepository.get_user(user_id)
