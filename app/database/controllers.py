"""
Не менее важный файл, тут будет происходить все взаимодействие с базой данных.

Тут пишешь все запросы к базе данных.
"""
from . import db_session
from app.database.models import User, Item

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
        pass

    @staticmethod
    def create_user(username, password):
        pass

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
