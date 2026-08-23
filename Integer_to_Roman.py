class RomanConverter:

    def __init__(self):
        self.val_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

    def int_to_roman(self, num: int) -> str:
        roman_num = ""
        for value, symbol in self.val_map:
            while num >= value:
                roman_num += symbol
                num -= value
        return roman_num


# Test
converter = RomanConverter()
number = input("Enter a number")
print(f"Integer: {number} -> Roman: {converter.int_to_roman(number)}")