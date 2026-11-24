import math

class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize dp array with infinity for all indices except 0
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Precompute the perfect squares up to n
        squares = [i * i for i in range(1, int(math.isqrt(n)) + 1)]
        
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
                
        return dp[n]