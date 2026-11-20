class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        # Create a combined string to find the longest palindromic prefix using KMP
        # We use a delimiter '#' that is not in the string to prevent overlap
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        
        # Build the LPS (Longest Proper Prefix which is also Suffix) array
        lps = [0] * len(combined)
        length = 0  # length of the previous longest prefix suffix
        
        for i in range(1, len(combined)):
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]
            if combined[i] == combined[length]:
                length += 1
            lps[i] = length
            
        # The length of the longest palindromic prefix is the last value in the LPS array
        longest_pal_prefix_len = lps[-1]
        
        # The characters after the longest palindromic prefix need to be reversed and prepended
        suffix = s[longest_pal_prefix_len:]
        return suffix[::-1] + s