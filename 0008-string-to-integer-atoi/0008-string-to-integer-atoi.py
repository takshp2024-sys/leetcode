class Solution:
    def myAtoi(self, s: str) -> int:
        # Constants for 32-bit signed integer boundaries
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        # Check if the string is empty or only contains whitespace
        if i == n:
            return 0
            
        # Step 2: Determine the sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
            
        # Step 3: Read the integer by skipping leading zeros
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow/underflow before actually appending the digit
            # If result > INT_MAX // 10, multiplying by 10 will definitely overflow.
            # If result == INT_MAX // 10, the digit must be <= 7 to not overflow (since INT_MAX ends in 7).
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
                
            result = result * 10 + digit
            i += 1
            
        # Apply the sign to the final result
        return sign * result