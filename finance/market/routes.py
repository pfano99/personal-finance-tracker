from flask import Blueprint, render_template, redirect, url_for

market = Blueprint("Market", __name__)


@market.route("/")
def market_dashboard():
    context = {
        "stocks": None
    }
    return render_template("market/market.html", context=context)
