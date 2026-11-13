class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        
        # Count the number of multiples of 5, 25, 125, etc.
        while n > 0:
            n //= 5
            count += n
            
        return count