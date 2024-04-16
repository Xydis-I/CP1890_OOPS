# Question 1 - Presentation Tier - Christian Barrett
from Question1_Business import Bus


def main():
    print("Product Manager\n")
    Bus.view_categories()
    print("\n"
          "COMMAND MENU\n"
          "view   - View products by category\n"
          "update - Update product price\n"
          "exit   - Exit program")

    while True:
        choice = input("\nCommand: ").lower()
        if choice == "exit":
            print("Bye!")
            break
        elif choice == "view":
            Bus.view_products()
        elif choice == "update":
            Bus.update_product()
        else:
            print("Invalid command. Please try again.")


if __name__ == '__main__':
    main()
