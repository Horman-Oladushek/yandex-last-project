from flask import Blueprint, redirect, render_template, flash, url_for

from app.forms.products_form import ProductForm
from app.database.repository import ProductRepository

products = Blueprint('products', __name__)


@products.route("/add", methods=["GET", "POST"], endpoint='create')
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        ProductRepository.create_product(
            form.title.data,
            form.description.data,
            form.price.data,
            form.quantity.data
        )
        flash("Товар добавлен", "success")
        return redirect(url_for("index.main"))
    return render_template('add_product.html', form=form)


@products.route("/update", methods=["GET"])
def update_product():
    flash('В разработке ;)', 'success')
    return redirect(url_for('index.main'))


@products.route("/delete/<int:product_id>", methods=["POST"])
def delete_product(product_id):
    if ProductRepository.delete_product(product_id):
        flash("Товар удален", "success")
        return redirect(url_for("index.main"))
    else:
        flash("Ошибка при удалении товара", "error")
        return redirect(url_for("index.main"))
