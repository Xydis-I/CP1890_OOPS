# Question 1
from dataclasses import dataclass


@dataclass
class Person:
    firstName: str
    lastName: str
    email: str

    @property
    def get_full_name(self):
        return f"{self.firstName} {self.lastName}"


@dataclass
class Customer(Person):
    number: str


@dataclass
class Employee(Person):
    ssn: str


def main():
    print("Customer/Employee Data Entry")

    while True:
        selection = input("\nCustomer or employee? (c/e): ").lower()

        print("\nDATA ENTRY")
        fName = input("First name: ").title()
        lName = input("Last name: ").title()
        email = input("Email: ")

        if selection == 'c':
            number = input("Number: ")
            data = Customer(fName, lName, email, number)
        elif selection == 'e':
            ssn = input("SSN: ")
            data = Employee(fName, lName, email, ssn)
        else:
            print("\nInvalid selection. Please try again.")
            continue

        if isinstance(data, Customer):
            print(f"\n"
                  f"CUSTOMER\n"
                  f"Name:       {data.get_full_name}\n"
                  f"Email:      {data.email}\n"
                  f"Number:     {data.number}")

        elif isinstance(data, Employee):
            print(f"\n"
                  f"EMPLOYEE\n"
                  f"Name:       {data.get_full_name}\n"
                  f"Email:      {data.email}\n"
                  f"SSN:        {data.ssn}")

        if input("\nContinue? (y/n): ").lower() != 'y':
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
