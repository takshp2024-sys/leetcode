class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        current_number = 0
        sign = 1  # 1 for positive, -1 for negative
        
        i = 0
        while i < len(s):
            char = s[i]
            
            if char.isdigit():
                # Build the multi-digit number
                current_number = current_number * 10 + int(char)
                
            elif char in "+-":
                # Apply the previous sign to the current number and add to result
                result += sign * current_number
                # Reset the number for the next calculation
                current_number = 0
                # Update the sign for the next number
                sign = 1 if char == '+' else -1
                
            elif char == '(':
                # Push the current result and sign onto the stack
                # This saves the state before entering the parentheses
                stack.append(result)
                stack.append(sign)
                # Reset for the sub-expression
                result = 0
                sign = 1
                
            elif char == ')':
                # Apply the sign to the current number and add to result
                result += sign * current_number
                current_number = 0
                
                # Pop the sign and previous result from the stack
                # The result inside the parentheses gets multiplied by the sign before '('
                current_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + current_sign * result
                
            i += 1
            
        # Add the last number to the result
        result += sign * current_number
        
        return result