class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign of x
        sign = -1 if x < 0 else 1
        
        # Work with the absolute value of x
        x = abs(x)
        
        # Reverse the integer mathematically
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
            
        # Apply the original sign
        reversed_x *= sign
        
        # Check for 32-bit integer overflow
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
            
        return reversed_x