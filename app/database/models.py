import sqlalchemy

from sqlalchemy.orm import DeclarativeBase
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


class User(Base, UserMixin):
    __tablename__ = "users"

    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        autoincrement=True,
        primary_key=True
    )

    login = sqlalchemy.Column(
        sqlalchemy.String(256),
        unique=True
    )

    password = sqlalchemy.Column(
        sqlalchemy.String(256)
    )

    def get_id(self):
        return self.user_id


class Product(Base):
    __tablename__ = "products"

    product_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        autoincrement=True,
        primary_key=True
    )

    title = sqlalchemy.Column(
        sqlalchemy.String(256)
    )

    description = sqlalchemy.Column(
        sqlalchemy.String(512)
    )

    price = sqlalchemy.Column(
        sqlalchemy.Integer
    )

    quantity = sqlalchemy.Column(
        sqlalchemy.Integer
    )
