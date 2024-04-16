# Question 1 - Business Tier - Christian Barrett
from Question1_Database import Db


def get_float(message: str) -> float:
    while True:
        num = input(message)
        try:
            return float(num)
        except ValueError:
            print("Invalid float. Please try again.")


def check_code(code: str) -> bool:
    return code.lower() in Db.select_product_codes()


class Bus:
    @staticmethod
    def view_categories() -> None:
        print(f"CATEGORIES\n"
              f"{' | '.join(Bus.get_categories())}")

    @staticmethod
    def get_categories() -> list:
        return Db.select_categories()

    @staticmethod
    def view_products() -> None:
        while True:
            category = input("Category name: ")

            if category.title() not in Bus.get_categories():
                print("Category not found. Please try again.\n")
            else:
                print(f"{'Code':<11}{'Name':<40}{'Price':>10}")
                print(61 * '-')
                for product in Db.select_products(category):
                    print(f"{product.code:<11}{product.name:<40}{product.price:>10.2f}")
                break

    @staticmethod
    def update_product() -> None:
        while True:
            code = input("Product code: ")
            if check_code(code):
                newPrice = get_float("New product price: ")
                Db.update_product(code, newPrice)
                break
            print("Invalid product code. Please try again.\n")


def main():
    Bus.view_products()
    print(check_code("strat"))
    print(check_code("asdasd"))


if __name__ == '__main__':
    main()
