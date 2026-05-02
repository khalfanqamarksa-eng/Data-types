# Get the starting number from the user
n = int(input("Enter the value of n: "))

# Print a header message
# .format(n, 1) replaces {0} with n and {1} with 1
print("numbers from {0} to {1} are: ".format(n, 1))

# Loop to print numbers backwards
# range(start, stop, step) 
# We stop at 0 so that 1 is the last number printed
for i in range(n, 0, -1):
    print(i)