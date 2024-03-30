"""
Не менее важный файл, тут будет происходить все взаимодействие с базой данных.

Тут пишешь все запросы к базе данных.
"""
from . import db_session
from app.database.models import User, Item
from app.database import user_parser as u_parser
from app.database import item_parser as i_parser
from flask import jsonify

class UserController:
    @staticmethod
    def get_user(user_id):
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        if not user:
            return None
        return user

    @staticmethod
    def get_all_users():
        session = db_session.create_session()
        users = session.query(User).all()
        return users

    @staticmethod
    def create_user():
        args = u_parser.parse_args()
        session = db_session.create_session()
        user = User(
            username=args['username'],
            password=args['password'],
            basket=args['basket'],
            is_superuser=args['is_superuser'] if args['is_superuser'] is True else False,
            is_active=args['is_active'] if args['is_active'] is True else False
        )
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def update_user(user_id, username, password):
        pass

    @staticmethod
    def delete_user(user_id):
        pass


class ItemController:
    @staticmethod
    def get_item(item_id):
        session = db_session.create_session()
        item = session.query(Item).get(item_id)
        if not item:
            return None
        return item

    @staticmethod
    def create_item(name):
        pass

    @staticmethod
    def update_item(item_id, name):
        pass

    @staticmethod
    def delete_item(item_id):
        pass
