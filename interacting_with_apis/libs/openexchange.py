import requests
# import functools
from cachetools import cached, TTLCache


class OpenExchangeCLient():
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    # @functools.lru_cache(maxsize=2)
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

    def convert(self, from_amount,from_currency, to_currency):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amount*to_rate
        else:
            return (from_amount/rates[from_currency])*to_currency