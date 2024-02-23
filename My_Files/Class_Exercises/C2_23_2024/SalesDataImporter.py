from dataclasses import dataclass

def main_menu():
    print("SALES DATA IMPORTER\n"
          "\n"
          "COMMAND MENU\n"
          "view   - View all sales\n"
          "add    - Add sales\n"
          "import - Import sales from file\n"
          "menu   - Show menu\n"
          "exit   - Exit program\n")


def interface():
    userInput = input("Please enter a command: ").lower()

    if userInput == "view":
        pass

    elif userInput == "add":
        pass

    elif userInput == "import":
        pass

    elif userInput == "menu":
        pass

    elif userInput == "exit":
        pass

    else:
        print("Invalid menu option.")


def main():
    main_menu()


if __name__ == '__main__':
    main()


@dataclass
class Region:
    name: str
    code: str

@dataclass
class Regions:
    regions = [Region("West", "wst"),
               Region("East", "est"),
               Region("Central", "cnt")]

