import os

from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from flask import jsonify, make_response
from app.database.handlers import user_handler, item_handler
from app.database import db_session
# Загружаем окружные переменные
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "secret string")
api = Api(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

api.add_resource(user_handler.ToDoListResource, '/api/v1/users/post')
api.add_resource(user_handler.ToDoAllResource, '/api/v1/users/all')
api.add_resource(user_handler.ToDoResource, '/api/v1/users/<int:user_id>')
api.add_resource(item_handler.ToDoListItems, '/api/v1/items/post')
db_session.global_init("app/db/shop-base.db")

from app import views
