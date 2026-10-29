class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        
        # If the needle is longer than the haystack, it can't be found
        if n > m:
            return -1
            
        # Iterate through the haystack, leaving enough room for the needle
        for i in range(m - n + 1):
            # Check if the substring of length n starting at i matches the needle
            if haystack[i:i+n] == needle:
                return i
                
        return -1