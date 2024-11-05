class Payment:
    def __init__(self, date, payment_method, amount):
        self.__date = date
        self.__payment_method = payment_method
        self.__amount = amount

    def get_amount(self):
        """Returns the payment amount."""
        return self.__amount

    def get_payment_method(self):
        """Returns the payment method."""
        return self.__payment_method
