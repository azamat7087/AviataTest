from django.urls import path
from connector.api.client.views import (ProvidersDataView, )

urlpatterns = [
    path('search/', ProvidersDataView.as_view({"post": "search"})),
    path('results/<str:search_id>/<str:currency>/', ProvidersDataView.as_view({"get": "get_providers_data"})),
]
