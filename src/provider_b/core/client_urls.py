from django.urls import path, include

urlpatterns = [
    path('', include('parser.api.client.urls')),
]
