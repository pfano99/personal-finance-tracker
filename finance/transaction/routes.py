from flask import Blueprint, redirect, url_for
from flask_login import login_required

transaction = Blueprint("Transaction", __name__)


@transaction.route("/", methods=["POST"])
@login_required
def add_transaction():
    return redirect(url_for("Main.index"))


@transaction.route("/", methods=["PUT"])
@login_required
def update_transaction():
    return redirect(url_for("Main.index"))
