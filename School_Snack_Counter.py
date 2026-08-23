from array import array

# Sets
box1 = {"Apple", "Chips", "Juice", "Cookie"}
box2 = {"Juice", "Sandwich", "Cookie", "Banana"}

# Add new snack
box1.add("Pretzels")

# Shared snacks (Intersection)
shared_snacks = box1.intersection(box2)
print(f"Shared Snacks: {shared_snacks}")

# Array of snack counts
snack_counts = array("i", [5, 12, 8, 12, 15])

# Add values to array
snack_counts.append(20)

# count() and reverse()
twelve_count = snack_counts.count(12)
snack_counts.reverse()

print(f"Occurrences of count 12: {twelve_count}")
print(f"Reversed Snack Counts Array: {list(snack_counts)}")