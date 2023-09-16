from django.urls import path

from rates.views import CurrencyConverterAPIView

app_name = "rates"

urlpatterns = [
    path("", CurrencyConverterAPIView.as_view(), name="exchanger"),
]
