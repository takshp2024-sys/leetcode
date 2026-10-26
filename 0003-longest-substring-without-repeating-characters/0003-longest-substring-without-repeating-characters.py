class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Maps character to its most recent index
        max_length = 0
        left = 0         # Left boundary of the sliding window

        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is already in the window, move the left boundary
            # to the right of the previous occurrence.
            if current_char in char_index and char_index[current_char] >= left:
                left = char_index[current_char] + 1
            
            # Update the character's latest index
            char_index[current_char] = right
            
            # Calculate the window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length