from rest_framework.response import Response
from rest_framework import status
import json
import time


def get_flights() -> Response:
    time.sleep(30)
    try:
        with open('parser/data/response_a.json') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return Response({"detail": "File not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(data, status=status.HTTP_200_OK)
