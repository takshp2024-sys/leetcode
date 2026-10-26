class Solution:
    def intToRoman(self, num: int) -> str:
        # Create a list of tuples mapping values to their Roman numeral symbols.
        # We include the subtractive forms (like CM, CD, XC, etc.) directly.
        # The list is ordered from largest to smallest.
        value_symbols = [
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
            (1, "I")
        ]
        
        roman = []
        
        # Iterate through the values from largest to smallest
        for value, symbol in value_symbols:
            # Check how many times the current value fits into num
            if num == 0:
                break
            
            count, num = divmod(num, value)
            
            # Append the symbol 'count' times
            roman.append(symbol * count)
            
        return "".join(roman)