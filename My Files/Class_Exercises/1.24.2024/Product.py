class Product:
    def __init__(self, name="", price=0.0, discount_percent=0):
        self.price: float = price
        self.name: str = name
        self.discountPercent: int = discount_percent

    def __post_init__(self):
        self.price = self.__price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Price cannot be less than 0")
        else:
            self.__price = price

    def get_discount_amount(self) -> float:
        return self.price * (self.discountPercent / 100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()
