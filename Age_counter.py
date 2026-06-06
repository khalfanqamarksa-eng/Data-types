try:
   
    age = int(input("Enter your age: "))
    
        
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    
    
    if age % 2 == 0:
        print(f"Result: {age} is an EVEN number.")
    else:
        print(f"Result: {age} is an ODD number.")

except ValueError as e:
    
    if str(e):
        print(f"Error: {e}")
    else:
        print("Error: Please enter a valid whole number.")

finally:
    
    print("Age check execution complete.")

    