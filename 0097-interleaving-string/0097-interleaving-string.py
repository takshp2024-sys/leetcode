class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        
        # If the lengths don't add up, interleaving is impossible
        if m + n != l:
            return False
            
        # dp[j] will represent whether s3[:i+j] is an interleaving of s1[:i] and s2[:j]
        # We initialize with the first row (i=0), meaning we only use s2
        dp = [False] * (n + 1)
        dp[0] = True
        
        # Fill the first row (s1 is empty)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        # Fill the rest of the DP table
        for i in range(1, m + 1):
            # Update the first column (s2 is empty)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            
            for j in range(1, n + 1):
                # Match character from s1 (coming from top in 2D table, which is dp[j] before update)
                match_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                # Match character from s2 (coming from left, which is dp[j-1] already updated)
                match_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                
                dp[j] = match_s1 or match_s2
                
        return dp[n]