from ClassPractice_1_15_2024 import Product

# Creating the products
product1 = Product("Stanley Hammer", 9.99, 5)
product2 = Product("Quartet Market", 2.00, 4)

print("Product Data")
print(f"Product Name:\t\t{product1.name}")
print(f"Product Price:\t\t{product1.price:.2f}")
print(f"Discount Percent:\t{product1.discountPercent}%")
print(f"Discount Amount:\t{product1.get_discount_amount():.2f}")
print(f"Discount Price: \t{product1.get_discount_price():.2f}")
