class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # dp[i] will store the (i+1)-th ugly number
        dp = [0] * n
        dp[0] = 1  # The first ugly number is 1
        
        # Pointers for 2, 3, and 5
        p2 = p3 = p5 = 0
        
        for i in range(1, n):
            # Calculate the next potential ugly numbers
            next2 = dp[p2] * 2
            next3 = dp[p3] * 3
            next5 = dp[p5] * 5
            
            # The next ugly number is the minimum of these
            next_ugly = min(next2, next3, next5)
            dp[i] = next_ugly
            
            # Advance the pointer(s) that produced the minimum
            # (Multiple pointers might produce the same value, so we advance all of them)
            if next_ugly == next2:
                p2 += 1
            if next_ugly == next3:
                p3 += 1
            if next_ugly == next5:
                p5 += 1
                
        return dp[n - 1]