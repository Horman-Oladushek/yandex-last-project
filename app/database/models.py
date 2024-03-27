from .db_session import SqlAlchemyBase
from sqlalchemy import Column, Integer, String
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


class Foo(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'foos'

    foo_id = Column(
        Integer, primary_key=True, autoincrement=True
    )

    name = Column(
        String, nullable=False
    )

# и т.д.
