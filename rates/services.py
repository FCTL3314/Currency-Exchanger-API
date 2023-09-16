from functools import cached_property

from common.exceprions import CurrencyNotFoundError
from common.services import IService
from core.currencyapi import client


class CurrencyConverterService(IService):
    def __init__(self, from_currency: str, to_currency: str, amount: float | str):
        self.currencies = self.load_currencies()
        self.validate_currencies((from_currency, to_currency))
        self.from_currency = from_currency
        self.to_currency = to_currency
        self._amount = amount

    def execute(self) -> float:
        return round(self.converted_currency, 2)

    def validate_currencies(self, currencies_to_validate):
        for currency in currencies_to_validate:
            if currency not in self.currencies:
                raise CurrencyNotFoundError(currency)

    @staticmethod
    def load_currencies() -> dict:
        return client.latest()["data"]

    @cached_property
    def amount(self) -> float:
        if isinstance(self._amount, str):
            return float(self._amount)
        return self._amount

    @property
    def from_currency_value(self) -> float:
        return self.currencies[self.from_currency]["value"]

    @property
    def to_currency_value(self) -> float:
        return self.currencies[self.to_currency]["value"]

    @property
    def converted_currency(self) -> float:
        return (self.to_currency_value / self.from_currency_value) * self.amount
