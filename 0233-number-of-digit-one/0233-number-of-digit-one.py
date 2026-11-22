class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1  # Start with the units place
        
        while i <= n:
            high = n // (i * 10)
            cur = (n // i) % 10
            low = n % i
            
            if cur == 0:
                # If cur is 0, only 'high' fully determines the count
                count += high * i
            elif cur == 1:
                # If cur is 1, 'high' plus the 'low' part determines the count
                count += high * i + (low + 1)
            else:
                # If cur is > 1, 'high + 1' fully determines the count
                count += (high + 1) * i
                
            i *= 10
            
        return count