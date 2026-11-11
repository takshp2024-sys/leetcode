class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        n = len(s)
        
        # dp[i] will be True if s[0:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always valid
        
        # Iterate through the string
        for i in range(1, n + 1):
            # Check all possible split points
            for j in range(i):
                # If the prefix s[0:j] is valid and the substring s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further if we found a valid split
                    
        return dp[n]