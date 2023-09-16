from functools import cached_property

from django.conf import settings

from common.exceprions import CurrencyNotFoundError
from common.services import IService
from core.currencyapi import client


class CurrencyConverterService(IService):
    """
    A service for converting one currency into another.
    """

    def __init__(self, from_currency: str, to_currency: str, amount: float | str):
        self.currencies = self.load_currencies()
        self.validate_currencies((from_currency, to_currency))
        self.from_currency = from_currency
        self.to_currency = to_currency
        self._amount = amount

    def execute(self) -> float:
        return round(self.converted_currency, settings.PRICE_ROUNDING)

    def validate_currencies(self, currencies_to_validate):
        """
        Checks if this currency is available for conversion.
        """
        for currency in currencies_to_validate:
            if currency not in self.currencies:
                raise CurrencyNotFoundError(currency)

    @staticmethod
    def load_currencies() -> dict:
        """
        Uploads currencies via api request.
        """
        return client.latest()["data"]

    @cached_property
    def amount(self) -> float:
        """
        Converts an attribute _amount to float if
        it is a string, returns it.
        """
        if isinstance(self._amount, str):
            return float(self._amount)
        return self._amount

    @property
    def from_currency_value(self) -> float:
        """
        Gets the currency that will be converted
        from the currencies attribute.
        """
        return self.currencies[self.from_currency]["value"]

    @property
    def to_currency_value(self) -> float:
        """
        Gets the currency to be converted from
        the currencies attribute.
        """
        return self.currencies[self.to_currency]["value"]

    @property
    def converted_currency(self) -> float:
        """
        Returns the converted currency.
        """
        return (self.to_currency_value / self.from_currency_value) * self.amount
