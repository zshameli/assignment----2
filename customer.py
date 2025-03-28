class Customer:

    def __init__(self, name, contact_info, is_loyalty_member=False):
        self.__name = name
        self.__contact_info = contact_info
        self.__is_loyalty_member = is_loyalty_member
        self.orders = []  # List to hold orders associated with this customer

    # Getters
    def get_name(self):
        """Gets the customer's name."""
        return self.__name

    def get_contact_info(self):
        """Gets the customer's contact information."""
        return self.__contact_info

    def get_is_loyalty_member(self):
        """Checks if the customer is a loyalty program member."""
        return self.__is_loyalty_member

    # Setters
    def set_is_loyalty_member(self, status):
        """Sets the customer's loyalty program membership status."""
        self.__is_loyalty_member = status

    def set_contact_info(self, new_contact_info):
        """Updates the customer's contact information."""
        self.__contact_info = new_contact_info

    # Methods
    def add_order(self, order):
        """Adds an order to the customer's order list."""
        self.orders.append(order)

    # String representation
    def __str__(self):
        return (f"Customer(Name: {self.__name}, Contact Info: {self.__contact_info}, "
                f"Loyalty Member: {self.__is_loyalty_member}, Orders: {len(self.orders)})")

    # Method to display full details as a dictionary (optional)
    def get_details(self):
        return {
            "Name": self.__name,
            "Contact Info": self.__contact_info,
            "Loyalty Member": self.__is_loyalty_member,
            "Orders Count": len(self.orders)
        }
