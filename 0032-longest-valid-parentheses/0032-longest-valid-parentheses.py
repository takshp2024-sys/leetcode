class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        max_len = 0
        
        # Pass 1: Left to Right
        # We treat '(' as +1 and ')' as -1. 
        # If left == right, we have a valid sequence.
        # If right > left, we have more closing brackets, which invalidates the current sequence.
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0
                
        # Pass 2: Right to Left
        # The first pass misses cases like "(()" where left > right at the end.
        # To catch these, we scan backwards. 
        # Here, if left > right, we reset.
        left = right = 0
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0
                
        return max_len