# Function to calculate subtotal
def get_subtotal(qty, price):
    return qty * price


# Function to calculate tax
def get_tax(subtotal):
    tax_rate = 0.08  # 8% sales tax
    return subtotal * tax_rate


# Function to display the receipt
def print_receipt(item, qty, price):
    subtotal = get_subtotal(qty, price)
    tax = get_tax(subtotal)
    total = subtotal + tax

    print("--- ART SUPPLIES STORE ---")
    print("Item purchased:", item)
    print("Quantity:", qty)
    print("Price per item: $" + str(price))
    print("--------------------------")
    print("Subtotal: $" + str(round(subtotal, 2)))
    print("Tax: $" + str(round(tax, 2)))
    print("Total Amount: $" + str(round(total, 2)))


# Test the program
item_name = "Paint Brushes Set"
item_count = 2
item_price = 15.50

print_receipt(item_name, item_count, item_price)