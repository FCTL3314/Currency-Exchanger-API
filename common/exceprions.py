class CurrencyNotFoundError(Exception):
    def __init__(self, currency_code: str):
        self.message = f"The currency with the code '{currency_code}' was not found."
        super().__init__(self.message)
