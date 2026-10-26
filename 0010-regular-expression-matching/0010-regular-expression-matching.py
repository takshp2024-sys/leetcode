class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] will be True if the first i characters of s 
        # match the first j characters of p.
        # We add 1 to lengths for the empty string base cases.
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Base case: Handle patterns like "a*", "a*b*", ".*" matching an empty string
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                # If the pattern has a '*', it can match zero occurrences of the preceding character.
                # So, we look at the value two columns back (ignoring "x*").
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                
                # Case 1: The current pattern character is a direct match or a '.' wildcard
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                    
                # Case 2: The current pattern character is '*'
                elif p[j - 1] == '*':
                    # Sub-case 2a: We use zero occurrences of the preceding character.
                    # We look at the state without "x*" (two columns back).
                    dp[i][j] = dp[i][j - 2]
                    
                    # Sub-case 2b: We use one or more occurrences.
                    # This is only possible if the character preceding '*' matches the current character in s.
                    # If it matches, we can "consume" a character from s and stay on the same pattern column.
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        # The final answer is whether the whole string s matches the whole pattern p
        return dp[len(s)][len(p)]