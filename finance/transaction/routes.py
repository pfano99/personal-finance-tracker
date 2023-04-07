from flask import Blueprint, redirect, url_for

transaction = Blueprint("Transaction", __name__)


@transaction.route("/", methods=["POST"])
def add_transaction():
    return redirect(url_for("Main.index"))


@transaction.route("/", methods=["PUT"])
def update_transaction():
    return redirect(url_for("Main.index"))
