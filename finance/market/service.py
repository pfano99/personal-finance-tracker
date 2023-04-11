from finance import db
from finance.models import Stock
from finance.stocks.stock_handler import StockHandler


def add_stock(ticker: str, bought_at: float, amount: float, user_id: int):
    stock = Stock(
        ticker=ticker,
        amount=amount,
        user_id=user_id,
        bought_at=bought_at
    )
    db.session.add(stock)
    db.session.commit()


def get_stocks_by_user_id(user_id: int) -> list:
    return Stock.query.filter_by(user_id=user_id)


def get_stocks_by_user_id_with_perc_change(user_id: int):
    user_stocks = get_stocks_by_user_id(user_id)

    sh = StockHandler()
    tickers = [stock.ticker for stock in user_stocks]
    batch = 0
    results = list()
    for _ in range(0, len(tickers), 3):
        res = sh.handle(tickers[batch:batch + 3])

        for stock in res:
            price = get_price(stock["ticker"], user_stocks)
            perc = calc_perc_diff(float(stock["price"]), price.bought_at)
            stock["perc"] = perc
            perc_price = price.amount + ((perc * price.amount) / 100)
            stock["perc_price"] = perc_price
            stock["perc_price_diff"] = perc_price - price.amount
        results += res
        batch += 3
    for i in results:
        print(i)
    return results


def get_price(ticker: str, user_stocks: list):
    for stock in user_stocks:
        if stock.ticker == ticker:
            return stock


def calc_perc_diff(current_price: float, bought_at_price: float) -> float:
    return ((current_price - bought_at_price) / bought_at_price) * 100
