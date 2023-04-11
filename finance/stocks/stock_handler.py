import requests


class StockHandler:

    def __init__(self, ):
        self.url = 'https://api.stockdata.org/v1/data/quote?symbols={}&api_token=' + StockHandler.init_token()

    def handle(self, tickers: list) -> list:
        data = ",".join(tickers[:3])
        res = requests.get(self.url.format(data))
        return res.json()["data"]

    @staticmethod
    def init_token() -> str:
        from finance.secrets import stock_api
        return stock_api.get("stock_data_org")
