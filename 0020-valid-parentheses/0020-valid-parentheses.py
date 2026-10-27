class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop from stack if it's not empty, else use a dummy value (like '#')
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped opening bracket matches the current closing bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched properly
        return not stack