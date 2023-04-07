from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required

from finance.auth.form import LoginForm, SignUpForm
from finance.auth.service import add_user, google_login, google_login_response, _login_user, _logout_user

auth = Blueprint('Auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        _login_user(email=form.email.data, password=form.password.data)
        return redirect(url_for('Main.index'))
    return render_template("auth/login.html", form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        add_user(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                 password=form.password.data, auth_type="default")
        return redirect(url_for('Main.index'))
    return render_template("auth/signup.html", form=form)


@auth.route("/google")
def google():
    return google_login(url_for('Auth.google_auth', _external=True))


@auth.route('/google/auth')
def google_auth():
    google_login_response()
    return redirect('/')


@auth.route("/logout")
@login_required
def logout():
    _logout_user()
    return redirect(url_for("Main.index"))
