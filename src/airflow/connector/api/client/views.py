from django.apps import apps
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from connector.serializers import (ProvidersDataSerializer, )
from connector.services.client.services import search_providers_data, get_providers_data


class ProvidersDataView(GenericViewSet):
    queryset = apps.get_model(app_label='connector', model_name='ProvidersData').objects.all()
    model = apps.get_model(app_label='connector', model_name='ProvidersData')
    serializer_class = ProvidersDataSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    permission_classes = [AllowAny, ]
    filter_fields = []
    lookup_field = "search_id"
    search_fields = []
    ordering_fields = ['id', 'updated_at', "created_at"]

    def search(self, request):
        search_id = search_providers_data(self.model)
        return Response({"search_id": search_id}, status=status.HTTP_200_OK)

    def get_providers_data(self, request, *args, **kwargs):
        providers_data = self.get_object()
        serializer = self.get_serializer_class()
        data = get_providers_data(providers_data, kwargs['currency'])
        result = serializer(providers_data, many=False).data
        result['items'] = data

        return Response(result, status=status.HTTP_200_OK)
