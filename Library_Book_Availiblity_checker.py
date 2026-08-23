books = ["1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby"]
counts = [3, 0, 5, 2]
late_fees = [1.5, 2.0, 0.5, 3.0]

# Pair books with counts using zip()
inventory = dict(zip(books, counts))

# Filter available books
available_books = list(filter(lambda item: item[1] > 0, inventory.items()))
print(f"Available Books: {available_books}")

# Update late fees using map() (10% penalty)
updated_fees = list(map(lambda fee: round(fee * 1.10, 2), late_fees))
print(f"Updated Late Fees: {updated_fees}")

# Stop program early when chosen book is unavailable
requested_book = "To Kill a Mockingbird"

for book, count in zip(books, counts):
    if book == requested_book and count == 0:
        print(f"ALERT: '{requested_book}' is unavailable! Stopping execution.")
        break
    print(f"Checking {book}: {count} available.")