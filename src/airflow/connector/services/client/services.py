from django.apps import apps

from connector.cron import update_exchange_rate
from connector.tasks import send_requests_to_providers


def search_providers_data(providers_data_model) -> str:

    providers_data = providers_data_model.objects.create()
    send_requests_to_providers.delay(providers_data.search_id)

    return providers_data.search_id


def filter_providers_data(providers_data, currency) -> list:

    data = list(filter(lambda d: d['pricing']['currency'] == currency, providers_data.items.copy()))
    data.sort(key=lambda e: float(e["pricing"]["total"]))

    return data


def get_exchange_rate():
    exchange_rate = apps.get_model(app_label="connector", model_name="ExchangeRate")

    if not exchange_rate.objects.count():
        update_exchange_rate()

    return exchange_rate.objects.first()


def add_price(data, currency) -> list:

    exchange_rate = get_exchange_rate()
    exchange_kzt = 1

    for rate in exchange_rate.rates["rates"]["item"]:
        if rate["title"] == currency and currency != "KZT":
            exchange_kzt = rate['description']

    for provider in data:
        amount = float(provider['pricing']['total']) * float(exchange_kzt)
        provider['price'] = {
            "amount": round(amount, 2),
            "currency": "KZT"
        }

    return data


def get_providers_data(providers_data, currency) -> list:

    data = filter_providers_data(providers_data, currency)
    data = add_price(data, currency)

    return data
