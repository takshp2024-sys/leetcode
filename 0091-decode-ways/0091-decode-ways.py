class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
            
        # prev2 represents dp[i-2] (ways to decode up to length i-2)
        # prev1 represents dp[i-1] (ways to decode up to length i-1)
        prev2 = 1
        prev1 = 1
        
        for i in range(1, len(s)):
            current = 0
            
            # Check if single digit is valid (not '0')
            if s[i] != '0':
                current += prev1
                
            # Check if two digits form a valid number between 10 and 26
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            # Move the pointers forward
            prev2 = prev1
            prev1 = current
            
        return prev1