from connector.celery import app
from django.apps import apps
import requests
import redis
from utils.choices import StatusChoices

providers_model = apps.get_model(app_label="connector", model_name="ProvidersData")


def check_completed(providers_data, search_id):
    redis_client = redis.Redis(host="localhost", port=6379, db=1)

    count = int(redis_client.get(f"count_{search_id}"))

    if count:
        redis_client.set(name=f"count_{search_id}", value=int(redis_client.get(f"count_{search_id}")) - 1)
    else:
        providers_data.status = StatusChoices.COMPLETED
        redis_client.close()

    return providers_data


@app.task
def send_request_to_provider(provider_url, search_id):
    response = requests.post(provider_url)

    providers_data = providers_model.objects.get(search_id=search_id)

    if providers_data.items:
        providers_data.items.extend(response.json())
    else:
        providers_data.items = response.json()

    providers_data = check_completed(providers_data, search_id)

    providers_data.save()


@app.task
def send_requests_to_providers(search_id) -> None:

    providers = [
        "http://127.0.0.1:9001/search/",
        "http://127.0.0.1:9002/search/",
    ]

    redis_client = redis.Redis(host="localhost", port=6379, db=1)
    redis_client.set(name=f"count_{search_id}", value=len(providers) - 1)

    for provider in providers:
        send_request_to_provider.delay(provider, search_id)

    redis_client.close()
