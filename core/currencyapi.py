import currencyapicom

from django.conf import settings

client = currencyapicom.Client(settings.CURRENCY_API_KEY)
