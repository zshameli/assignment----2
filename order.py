from invoice import Invoice
class Order:
    def __init__(self, customer, date):
        self.__customer = customer
        self.__date = date
        self.__ebooks = []
        self.__total_amount = 0
        self.__invoice = None

    def add_ebook(self, ebook):
        self.__ebooks.append(ebook)
        self.__total_amount += ebook.get_price()

    def calculate_total_with_discount(self, discount_rate):
        """Calculates the total with a given discount rate."""
        return self.__total_amount * (1 - discount_rate)

    def generate_invoice(self):
        invoice_id = f"INV-{self.__date.replace('-', '')}"  
        invoice_total = self.__total_amount
        self.__invoice = Invoice(invoice_id, invoice_total)
    
    def get_invoice(self):
        """Returns the generated invoice."""
        return self.__invoice
