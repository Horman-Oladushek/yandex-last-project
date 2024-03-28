from .db_session import SqlAlchemyBase
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy_serializer import SerializerMixin


"""
Здесь пишешь все модели.
Старайся придерживаться такого оформления в плане отступов, 
это хороший тон программиста.
"""


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    user_id = Column(
        Integer, primary_key=True, autoincrement=True
    )

    username = Column(
        String, nullable=False
    )

    password = Column(
        String, nullable=False
    )

    basket = Column(
        String, nullable=True
    )

    #Here Boolean is a type of Column.
    is_superuser = Column(
        Boolean, nullable=False
    )

    is_active = Column(
        Boolean, nullable=False
    )


class Item(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'items'

    item_id = Column(
        Integer, primary_key=True, autoincrement=True
    )

    name = Column(
        String, nullable=False
    )

    description = Column(
        String, nullable=True
    )

    price = Column(
        Integer, nullable=False
    )


    discount = Column(
        String, nullable=False
    )

    is_sale = Column(
        Boolean, nullable=False
    )

