from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from finance.market.form import StockForm
from finance.market.service import add_stock, get_stocks_by_user_id, get_stocks_by_user_id_with_perc_change

market = Blueprint("Market", __name__)


@market.route("/")
@login_required
def market_dashboard():
    form = StockForm()
    context = {
        "stocks": get_stocks_by_user_id_with_perc_change(current_user.id),
        "form": form
    }
    return render_template("market/market.html", context=context)


@market.route("/add", methods=['POST'])
@login_required
def post_add_stock():
    form = StockForm()
    if form.validate_on_submit():
        add_stock(ticker=form.ticker.data, bought_at=form.bought_at.data, amount=form.amount.data,
                  user_id=current_user.id)
    return redirect(url_for("Market.market_dashboard"))
