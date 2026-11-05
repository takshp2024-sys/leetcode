from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
            
        # Dictionary to keep track of the counts of characters in t
        dict_t = Counter(t)
        
        # Number of unique characters in t that need to be present in the window
        required = len(dict_t)
        
        # Left and Right pointers for the sliding window
        left, right = 0, 0
        
        # Number of unique characters in the current window that match the required counts
        formed = 0
        
        # Dictionary to keep track of the counts of characters in the current window
        window_counts = {}
        
        # Tuple to store the result: (window length, left, right)
        ans = float("inf"), None, None
        
        while right < len(s):
            # Add the current character to the window
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the current character's count matches the required count in t, increment 'formed'
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
                
            # Try to shrink the window from the left while it's valid
            while left <= right and formed == required:
                char = s[left]
                
                # Save the smallest window so far
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                    
                # Remove the character at 'left' from the window
                window_counts[char] -= 1
                
                # If the character is in t and its count drops below the required count, decrement 'formed'
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                    
                # Move the left pointer forward to shrink the window
                left += 1
                
            # Expand the window to the right
            right += 1
            
        # If ans[0] is still infinity, no valid window was found
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]