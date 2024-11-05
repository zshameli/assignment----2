from shopping_cart_item import ShoppingCartItem
class ShoppingCart:
    def __init__(self, customer):
        self.__customer = customer
        self.__items = []

    def add_item(self, ebook, quantity):
        item = ShoppingCartItem(ebook, quantity)
        self.__items.append(item)

    def get_items(self):
        """Returns the list of items in the cart."""
        return self.__items

    def remove_item(self, ebook):
        """Removes a specific item from the cart."""
        self.__items = [item for item in self.__items if item.get_ebook() != ebook]

    def calculate_total(self):
        """Calculates the total amount for all items in the cart."""
        return sum(item.get_ebook().get_price() * item.get_quantity() for item in self.__items)

    def __str__(self):
        items_list = ", ".join([str(item) for item in self.__items])
        return f"ShoppingCart(Customer: {self.__customer.get_name()}, Items: [{items_list}])"
