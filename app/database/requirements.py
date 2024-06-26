"""
все запросы к базе данных.
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
    def create_user(user):
        args = u_parser.parse_args()
        session = db_session.create_session()
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
    def create_item(item):
        session = db_session.create_session()
        session.add(item)
        session.commit()

    @staticmethod
    def update_item(item_id, name):
        pass

    @staticmethod
    def delete_item(item_id):
        pass
