# F-Strings with format specifications
fp_number = 12345.6789
fp_number2 = 234512345.6789
fp_number3 = .6789

dc_number = 6789

# [field_width][comma].[decimal_places][type_code]
#                     .2f - floating-point number
#                       d - integer
#                       % - percentage
#                       e - scientific notation

# Base
print(f"{fp_number:.2f}")
print("{:.2f}".format(fp_number))

# Add Commas
print(f"{fp_number:,.2f}")

# Justification
print(f"{fp_number:15,.2f}")
print(f"{fp_number2:15,.2f}")

# Different type codes
print(f"{fp_number3:.0%}")
print(f"{fp_number3:.1%}")

print(f"{dc_number:d}")
print(f"{dc_number:,d}")
print(f"{dc_number:10,d}")

# Formatting String Literals
print(f"{'Description':15} {'Price':>10} {'Qty':>5}")
print(f"{'Legend of Zelda':15} {10.99:10.2f} {3:5d}")

# Locales
# SetLocale()
# Currency()
# Format()
import locale
locale.setlocale(locale.LC_ALL, 'en-ca')
print(locale.currency(1222, symbol=True, grouping=True, international=True))
