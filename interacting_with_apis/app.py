# import requests
import time
from interacting_with_apis.libs.openexchange import OpenExchangeCLient

APP_ID = "0e3b25b23e164013adb87b5c5af2c2d0"
# ENDPOINT = "https://openexchangerates.org/api/latest.json"
#
# response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
# exchange_rates = response.json()['rates']

client = OpenExchangeCLient(APP_ID)

usd_amount = 1000
start_time = time.time()
# gbp_amount = usd_amount * exchange_rates["GBP"]
gbp_amount = client.convert(usd_amount, "USD", "GBP")
print(f"total TIme : {time.time() - start_time}")


start_time = time.time()
# gbp_amount = usd_amount * exchange_rates["GBP"]
gbp_amount = client.convert(usd_amount, "USD", "GBP")
print(f"total TIme : {time.time() - start_time}")


start_time = time.time()
# gbp_amount = usd_amount * exchange_rates["GBP"]
gbp_amount = client.convert(usd_amount, "USD", "GBP")
print(f"total TIme : {time.time() - start_time}")
print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")
