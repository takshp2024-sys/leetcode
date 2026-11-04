class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create a DP table of size (m + 1) x (n + 1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: converting to/from an empty string
        # It takes i deletions to convert word1[:i] to an empty string
        for i in range(m + 1):
            dp[i][0] = i
            
        # It takes j insertions to convert an empty string to word2[:j]
        for j in range(n + 1):
            dp[0][j] = j
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the characters match, no new operation is needed
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # We take the minimum of the three operations:
                    # 1. Replace: dp[i-1][j-1] + 1
                    # 2. Delete:  dp[i-1][j] + 1
                    # 3. Insert:  dp[i][j-1] + 1
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    
        return dp[m][n]