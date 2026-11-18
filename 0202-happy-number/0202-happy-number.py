class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            
            # Calculate the sum of the squares of the digits
            current_sum = 0
            while n > 0:
                digit = n % 10
                current_sum += digit * digit
                n //= 10
                
            n = current_sum
            
        return n == 1