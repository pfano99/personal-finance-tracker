from flask import Blueprint, render_template, request
from finance.models import User
from finance.auth.form import SignUpForm

user = Blueprint("User", __name__)


@user.route("/profile/<int:user_id>", methods=['GET', 'POST'])
def user_profile(user_id: int):
    user = User.query.get(user_id)
    form = SignUpForm()
    if request.method == 'GET':
        form.first_name.data = user.first_name
        form.last_name.data = user.last_name
        form.email.data = user.email

    if form.validate_on_submit():
        pass
    return render_template("profile/user_profile.html", form=form)
