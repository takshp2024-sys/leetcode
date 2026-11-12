class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Pop the top two elements. The first popped is the right operand.
                right = stack.pop()
                left = stack.pop()
                
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    # Truncate towards zero using int() instead of Python's floor division (//)
                    stack.append(int(left / right))
            else:
                # If it's a number, convert to int and push to stack
                stack.append(int(token))
                
        return stack[0]