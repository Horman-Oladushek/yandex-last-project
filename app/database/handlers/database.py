from app.database import db_session
from app.database.models import User, Item

def get_user(user_id):
    session = db_session.create_session()
    todo = session.query(User).get(user_id)
    if not todo:
        return None
    return todo

def get_item(item_id):
    session = db_session.create_session()
    todo = session.query(Item).get(item_id)
    if not todo:
        return None
    return todo