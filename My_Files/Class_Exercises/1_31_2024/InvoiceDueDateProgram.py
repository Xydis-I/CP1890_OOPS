from datetime import datetime, timedelta


def main():
    while True:
        print("The Invoice Due Date program\n")
        invoiceDate = get_date()
        print(f"\nInvoice Date: {invoiceDate:%B %d, %Y}")
        dueDate = invoiceDate + timedelta(days=30)
        print(f"Due Date: {dueDate:%B %d, %Y}")
        print(f"Current Date: {datetime.now():%B %d, %Y}")
        print(f"\nThis invoice is {(datetime.now() - dueDate).days} day(s) overdue.")

        if input("\nContinue? (y/n): ").lower() != 'y':
            break


def get_date() -> datetime:
    while True:
        try:
            dueDate = datetime.strptime(input("Enter the invoice date (MM/DD/YY): "), "%m/%d/%y")
            return dueDate
        except ValueError:
            print("Invalid date. Please try again.")


if __name__ == "__main__":
    main()
