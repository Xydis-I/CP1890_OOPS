import locale as lc

while True:
    monInvestment = float(input("Enter monthly investment:\t "))
    rate = float(input("Enter yearly interest rate:\t "))
    years = int(input("Enter number of years:\t\t "))

    lc.setlocale(lc.LC_ALL, 'en-ca')

    total = 0
    for year in range(years * 12):
        total += monInvestment
        total *= (1 + (rate/12/100))

    print(f"\nMonthly investment: {lc.currency(monInvestment, grouping=True):>12s}")
    print(f"Interest rate: {rate:>17.1f}")
    print(f"Years: {years:>25d}")
    print(f"Future Value: {lc.currency(total, grouping=True): >18s}")

    if input("\nContinue? (y/n) ").lower() != 'y':
        break
