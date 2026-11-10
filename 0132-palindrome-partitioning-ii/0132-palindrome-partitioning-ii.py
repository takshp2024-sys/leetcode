class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # is_pal[i][j] is True if s[i:j+1] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        
        # dp[i] will store the minimum cuts needed for s[0:i+1]
        # Initialize with the maximum possible cuts (i), as a string of length i+1 can always be cut i times
        dp = [i for i in range(n)]
        
        for j in range(n):
            # Check all substrings ending at j
            for i in range(j, -1, -1):
                # A substring s[i:j+1] is a palindrome if:
                # 1. The characters at i and j match
                # 2. The inner substring s[i+1:j] is a palindrome (or length <= 2)
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
                    
                    # If s[0:j+1] is a palindrome, no cuts are needed (0 cuts)
                    if i == 0:
                        dp[j] = 0
                    else:
                        # Otherwise, we can cut at i-1 and add 1 cut.
                        # We take the minimum over all valid palindromic prefixes ending at j.
                        dp[j] = min(dp[j], dp[i - 1] + 1)
                        
        return dp[n - 1]