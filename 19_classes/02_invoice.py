class Invoice:
    vat = 1.18

    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items += [(item, price)]

    def total(self):
        return int(sum([i[1] for i in self.items]) * Invoice.vat)

    @classmethod
    def price_with_vat(cls, price):
        return int(price * Invoice.vat)

print(Invoice.price_with_vat(20))

