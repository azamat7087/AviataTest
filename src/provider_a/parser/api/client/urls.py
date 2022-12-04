from django.urls import path
from parser.api.client.views import (SearchFlightsView, )

urlpatterns = [
    path('search/', SearchFlightsView.as_view()),
]
