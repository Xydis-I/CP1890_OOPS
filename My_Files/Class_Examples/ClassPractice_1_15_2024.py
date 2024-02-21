from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    discountPercent: int

    def get_discount_amount(self) -> float:
        return self.price * (self.discountPercent / 100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()
