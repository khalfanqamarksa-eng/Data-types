number = int(input("Enter a number: "))
count = 0

# Using a while loop to count digits
# We divide by 10 each time to remove the last digit
temp = abs(number) # Use absolute value to handle negative numbers
while temp > 0:
    temp = temp // 10
    count += 1

if number == 0: count = 1 # Special case for zero

print(f"Total digits: {count}")