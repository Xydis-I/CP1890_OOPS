from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    discount: float

    def get_name(self):
        return self.name

    def get_discount_amount(self) -> float:
        return self.price * (self.discount / 100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()


@dataclass
class Movie(Product):
    year: int

    def get_year(self) -> int:
        return self.year


@dataclass
class Book(Product):
    author: str

    def get_author(self) -> str:
        return self.author


def get_products():
    return [Product("Stanley 13 Ounce Wood Hammer", 9.88, 50),
            Movie("The Holy Grail - DVD", 9.60, 50, 1975),
            Book("Ready Player One", 12.44, 30, "Ernest Cline")]


def main():
    products = [Product("Stanley 13 Ounce Wood Hammer", 9.88, 50),
                Movie("The Holy Grail - DVD", 9.60, 50, 1975),
                Book("Ready Player One", 12.44, 30, "Ernest Cline")]

    # Could use isinstance if order was reversed, since it counts children.
    for product in products:
        print("PRODUCT DATA")
        if type(product) is Product:
            print(f"Name:              {product.get_name()}\n"
                  f"Discount price:    {product.get_discount_price():.2f}"
                  f"\n")

        elif type(product) is Movie:
            print(f"Name:              {product.get_name()}\n"
                  f"Year:              {product.get_year()}\n"
                  f"Discount price:    {product.get_discount_price():.2f}"
                  f"\n")

        elif type(product) is Book:
            print(f"Name:              {product.get_name()}\n"
                  f"Author:            {product.get_author()}\n"
                  f"Discount price:    {product.get_discount_price():.2f}"
                  f"\n")


if __name__ == "__main__":
    main()