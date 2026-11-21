class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        # Initialize the operator as '+' to handle the first number correctly
        operation = '+' 
        
        for i, char in enumerate(s):
            if char.isdigit():
                # Build the multi-digit number
                current_number = current_number * 10 + int(char)
                
            # If the character is an operator or we are at the last character of the string
            if char in "+-*/" or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    # Pop the last number, multiply, and push back
                    stack.append(stack.pop() * current_number)
                elif operation == '/':
                    # Pop the last number, divide, and push back
                    # int() truncates toward zero, which is what the problem requires
                    stack.append(int(stack.pop() / current_number))
                    
                # Update the operation to the current character
                operation = char
                # Reset the current number for the next build
                current_number = 0
                
        # The result is the sum of all elements in the stack
        return sum(stack)