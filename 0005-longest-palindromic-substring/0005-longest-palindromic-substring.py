class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            # Expand as long as the characters match and we are within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindromes (single character center)
            len1 = expand_around_center(i, i)
            # Even length palindromes (two character center)
            len2 = expand_around_center(i, i + 1)
            
            # Get the maximum length from the two types of centers
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update the start and end indices
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # Return the longest palindromic substring
        return s[start:end + 1]