from flask import Blueprint, render_template

from app.database.repository import ProductRepository

index = Blueprint('index', __name__)


@index.route('/', methods=['GET'], endpoint='main')
def index_page():
    products = ProductRepository.get_products()
    return render_template('index.html', data=products)
