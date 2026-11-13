class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
            
        # Determine the sign of the result
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        
        # Work with absolute values
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Calculate the integer part
        integer_part = numerator // denominator
        remainder = numerator % denominator
        
        # If there is no fractional part, return the integer
        if remainder == 0:
            return sign + str(integer_part)
            
        # Build the fractional part
        decimal_part = []
        # Dictionary to store the remainder and its index in the decimal part
        remainder_map = {}
        
        while remainder != 0:
            # If we have seen this remainder before, we found a repeating cycle
            if remainder in remainder_map:
                start = remainder_map[remainder]
                decimal_part.insert(start, "(")
                decimal_part.append(")")
                break
                
            # Record the current remainder and its position
            remainder_map[remainder] = len(decimal_part)
            
            remainder *= 10
            decimal_part.append(str(remainder // denominator))
            remainder %= denominator
            
        return sign + str(integer_part) + "." + "".join(decimal_part)