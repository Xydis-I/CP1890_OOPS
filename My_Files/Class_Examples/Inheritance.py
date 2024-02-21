from dataclasses import dataclass


@dataclass
class Product:
    name: str = ""
    price: float = 0.0
    discountAmount: float = 0

    def get_discount_amount(self) -> float:
        return self.price * (self.discountAmount/100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()

    def get_description(self) -> str:
        return self.name


# class Book(Product):
#     def __init__(self, name="", price=0.0, discountAmount=0, author=""):
#         Product.__init__(self, name, price, discountAmount)
#         self.author = author
#
#     def get_description(self) -> str:
#         return (f"{Product.get_description(self)}\n"
#                 f"  by {self.author}")


@dataclass
class Book(Product):
    author: str = ""

    def get_description(self) -> str:
        return (f"{Product.get_description(self)}\n"
                f"  by {self.author}")


@dataclass
class Movie(Product):
    year: int = 0

    def get_description(self) -> str:
        return (f"{Product.get_description(self)}\n"
                f"  {self.year}")


def main():
    product1 = Product("Quartet Marker", 2.99, 20)
    book1 = Book("Ready Player One", 19.99, 20, "Ernest Cline")
    movie1 = Movie("Ready Player One", 19.99, 20, 2018)

    print(book1.get_description())
    print()
    print(product1.get_description())
    print()
    print(movie1.get_description())


if __name__ == "__main__":
    main()
