from werkzeug.security import generate_password_hash

from .engine import EngineController
from .models import User, Product


class UserRepository:
    database_controller = EngineController()

    @classmethod
    def get_users(cls) -> list[User]:
        session = cls.database_controller.create_session()
        users = session.query(User).all()
        session.close()
        return users

    @classmethod
    def get_user(cls, user_id: int) -> User:
        session = cls.database_controller.create_session()
        user = session.query(User).filter(User.user_id == user_id).first()
        session.close()
        return user

    @classmethod
    def get_user_by_login(cls, login: str) -> User:
        session = cls.database_controller.create_session()
        user = session.query(User).filter(User.login == login).first()
        session.close()
        return user

    @classmethod
    def create_user(cls, login: str, password: str) -> None:
        session = cls.database_controller.create_session()
        password = generate_password_hash(password)
        user = User(
            login=login,
            password=password
        )
        session.add(user)
        session.commit()
        session.close()


class ProductRepository:
    databese_controller = EngineController()

    @classmethod
    def get_products(cls) -> list[Product]:
        session = cls.databese_controller.create_session()
        products = session.query(Product).all()
        session.close()
        return products

    @classmethod
    def get_product(cls, product_id: int) -> Product:
        session = cls.databese_controller.create_session()
        product = session.query(Product).filter(
            Product.product_id == product_id
        ).first()
        session.close()
        return product

    @classmethod
    def create_product(cls, title: str, description: str, price: int, quantity: int) -> None:
        session = cls.databese_controller.create_session()
        product = Product(
            title=title,
            description=description,
            price=price,
            quantity=quantity
        )
        session.add(product)
        session.commit()
        session.close()

    @classmethod
    def delete_product(cls, product_id: int) -> bool:
        session = cls.databese_controller.create_session()
        product = session.query(Product).filter(
            Product.product_id == product_id
        ).first()
        if product:
            session.delete(product)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False
