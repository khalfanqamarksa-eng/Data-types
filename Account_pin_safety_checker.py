class AccountPINChecker:

    def __init__(self, account_holder, pin):
        self.account_holder = account_holder
        self.__pin = pin  # Private attribute

    # Setter method for updating private data safely
    def set_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print("Error: Old PIN is incorrect.")
        elif len(str(new_pin)) != 4:
            print("Error: PIN must be 4 digits.")
        else:
            self.__pin = new_pin
            print("PIN updated successfully.")

    # __str__ function to control output with print()
    def __str__(self):
        masked_pin = "*" * len(str(self.__pin))
        return f"Account Holder: {self.account_holder} | PIN: {masked_pin}"


# Test
acc = AccountPINChecker("Alex", 1234)

# Display object using __str__
print(acc)

# Update PIN safely via setter
acc.set_pin(1234, 5678)
print(acc)