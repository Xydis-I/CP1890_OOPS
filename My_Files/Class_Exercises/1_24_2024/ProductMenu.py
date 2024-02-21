from Product import Product


def get_int(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid number. Please Try Again.")


def display_products(products: list):
    for n, product in enumerate(products, 1):
        print(f"{n}. {product.name}")


def product_info(products: list, index: int):
    try:
        product = products[index]
        print(f"Name:\t\t\t  {product.name}")
        print(f"Price:\t\t\t  {product.price}")
        print(f"Discount percent: {product.discountPercent}%")
        print(f"Discount amount:  {product.get_discount_amount():.2f}")
        print(f"Discount price:   {product.get_discount_price():.2f}")
    except IndexError:
        print("Product does not exist.")


def main():
    print("The Product Viewer program")

    products = [Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Product('National Hardware 3/4" Wire Nails', 8.99, 20),
                Product('Economy Duct Tape, 60 yds, Silver', 5.99, 30)]

    print("\nPRODUCTS")
    display_products(products)

    while True:
        product_number = get_int("\nEnter product number: ")

        print("\nPRODUCT DATA")
        product_info(products, product_number - 1)

        if input("\nView another product? (y/n): ").lower() != 'y':
            break


if __name__ == "__main__":
    main()
