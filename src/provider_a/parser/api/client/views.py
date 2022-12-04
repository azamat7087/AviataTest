from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from parser.services.client.services import get_flights


class SearchFlightsView(APIView):
    permission_classes = [AllowAny, ]

    @staticmethod
    def post(request):
        return get_flights()
