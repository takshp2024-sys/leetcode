class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
            
        # Determine the sign (True if one is negative, False if both are same)
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # Subtract the largest possible shifted divisor from the dividend
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)
                quotient |= (1 << i)
                
        # Apply the sign without using multiplication
        if is_negative:
            quotient = -quotient
            
        return quotient