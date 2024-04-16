# Question 1 - Database Tier - Christian Barrett
from dataclasses import dataclass
import sqlite3
from contextlib import closing


@dataclass
class Product:
    code: str
    name: str
    price: float


class Db:
    @staticmethod
    def select_categories() -> list:
        with closing(sqlite3.connect('guitar_shop.sqlite')) as conn:
            c = conn.cursor()
            return [x[0] for x in c.execute("""SELECT categoryName FROM Category;""").fetchall()]

    @staticmethod
    def select_products(category: str) -> list:
        products = []
        with closing(sqlite3.connect('guitar_shop.sqlite')) as conn:
            c = conn.cursor()
            productData = c.execute(f"""SELECT productCode,productName,listPrice
                                        FROM Product P
                                        JOIN Category C on P.categoryID = C.categoryID
                                        WHERE categoryName = "{category.title()}"
                                        ORDER BY productName ASC;""").fetchall()
            for data in productData:
                products.append(Product(data[0], data[1], data[2]))
            return products

    @staticmethod
    def update_product(productCode: str, newPrice: float) -> None:
        with closing(sqlite3.connect('guitar_shop.sqlite')) as conn:
            c = conn.cursor()
            c.execute(f"""UPDATE Product SET listPrice = {newPrice} WHERE productCode = "{productCode.lower()}";""")
            conn.commit()

            print("Product updated.")

    @staticmethod
    def select_product_codes() -> list:
        with closing(sqlite3.connect('guitar_shop.sqlite')) as conn:
            c = conn.cursor()
            return [x[0] for x in c.execute("""SELECT productCode FROM Product;""").fetchall()]


def main():
    print(Db.select_categories())
    print(Db.select_products("basses"))
    Db.update_product("hofner", 499.99)
    print(Db.select_products("basses"))
    print(Db.select_product_codes())


if __name__ == '__main__':
    main()
