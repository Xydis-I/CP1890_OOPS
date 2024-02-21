class Product:
    def __init__(self, name="", price=0.0, discount_percent=0):
        self.name = name
        self.price = price
        self.discountPercent = discount_percent

    def get_discount_amount(self) -> float:
        return self.price * (self.discountPercent / 100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()
