from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.exceprions import CurrencyNotFoundError
from rates.serializers import CurrencyConverterSerializer
from rates.services import CurrencyConverterService


class CurrencyConverterAPIView(APIView):
    serializer_class = CurrencyConverterSerializer
    service_class = CurrencyConverterService

    def get(self, request):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        try:
            service = self.service_class(
                serializer.data["_from"],
                serializer.data["to"],
                serializer.data["value"],
            )
            return Response(
                {"result": service.execute()},
                status.HTTP_200_OK
            )
        except CurrencyNotFoundError as error:
            return Response(
                {"detail": error.message},
                status.HTTP_400_BAD_REQUEST,
            )



