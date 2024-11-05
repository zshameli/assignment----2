class ShoppingCartItem:
    """
    Class to represent an Item in the Shopping Cart.
    """

    def __init__(self, ebook, quantity):
        self.__ebook = ebook
        self.__quantity = quantity

    # Getters
    def get_ebook(self):
        """Gets the e-book associated with the shopping cart item."""
        return self.__ebook

    def get_quantity(self):
        """Gets the quantity of the item."""
        return self.__quantity

    # Setters
    def set_quantity(self, quantity):
        """Sets a new quantity for the item."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = quantity

    def __str__(self):
        return f"ShoppingCartItem(EBook: {self.__ebook.get_title()}, Quantity: {self.__quantity})"
