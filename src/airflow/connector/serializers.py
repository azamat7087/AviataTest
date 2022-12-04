from django.apps import apps
from rest_framework import serializers


class ProvidersDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model(app_label="connector", model_name="ProvidersData")
        fields = (
            'search_id', 'status',
        )
