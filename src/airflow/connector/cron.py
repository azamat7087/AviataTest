from datetime import datetime

import requests
import xmltodict
from django.apps import apps


def update_exchange_rate():
    date = datetime.today().strftime("%d.%m.%Y")
    url = f"https://www.nationalbank.kz/rss/get_rates.cfm?fdate={date}"
    exchange_rate_model = apps.get_model(app_label="connector", model_name="ExchangeRate")

    response = requests.get(url)
    if response.status_code == 200:
        data = xmltodict.parse(response.text)
        exchange_rate_model.objects.create(rates=data)
