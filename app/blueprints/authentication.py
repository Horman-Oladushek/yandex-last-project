from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import check_password_hash

from app.database.repository import UserRepository
from app.forms.authentication_form import RegisterForm, LoginForm

authentication = Blueprint('authentication', __name__)


@authentication.route("/register", methods=["GET", "POST"], endpoint='register')
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        UserRepository.create_user(
            form.login.data,
            form.password.data
        )
        flash("Вы создали аккаунт", "success")
        return redirect(url_for("authentication.login"))
    return render_template("register.html", form=form)


@authentication.route("/login", methods=["GET", "POST"], endpoint='login')
def login_user_page():
    if current_user.is_authenticated:
        return redirect(url_for('index.main'))
    form = LoginForm()
    if form.validate_on_submit():
        user = UserRepository.get_user_by_login(form.login.data)
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("index.main"))
            else:
                flash("Invalid password", "error")
                redirect(url_for("authentication.login"))
        else:
            flash("Invalid email or account does not exist", "error")
            return redirect(url_for("authentication.login"))
    return render_template("login.html", form=form)


@login_required
@authentication.route("/logout", methods=["GET"], endpoint='logout')
def logout_user_page():
    logout_user()
    return redirect(url_for("index.main"))
