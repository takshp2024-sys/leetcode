class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if the first i characters of s match the first j characters of p
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: Empty string matches empty pattern
        dp[0][0] = True
        
        # Base case: Empty string matching a pattern with '*'
        # '*' can match an empty sequence, so if p[j-1] is '*', it depends on dp[0][j-2] (or j-1)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: The current pattern character is '?' or matches the current string character
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    
                # Case 2: The current pattern character is '*'
                elif p[j - 1] == '*':
                    # '*' can match zero characters (dp[i][j-1]) 
                    # OR it can match one or more characters (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                    
        return dp[m][n]