class Invoice:
    def __init__(self, invoice_id, invoice_total):
        self.__invoice_id = invoice_id
        self.__invoice_total = invoice_total

    def get_invoice_total(self):
        return self.__invoice_total
