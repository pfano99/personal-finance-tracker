from flask import Blueprint

account = Blueprint("Account", __name__)


@account.route("/add")
def add_account():
    pass
