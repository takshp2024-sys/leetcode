class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] will store the number of distinct subsequences of s[:i] that equal t[:j]
        dp = [0] * (n + 1)
        
        # Base case: An empty string t can be formed by any string s in exactly 1 way (by deleting all characters)
        dp[0] = 1
        
        # Iterate through the characters of s
        for i in range(1, m + 1):
            # Iterate backwards through t to avoid overwriting values we need for the current step
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] = dp[j] + dp[j - 1]
                    
        return dp[n]