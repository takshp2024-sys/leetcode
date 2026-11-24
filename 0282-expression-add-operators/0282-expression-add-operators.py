class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        
        def backtrack(index: int, prev_operand: int, current_value: int, expression: str):
            # Base case: If we've processed all digits
            if index == len(num):
                if current_value == target:
                    result.append(expression)
                return
                
            # Try all possible lengths for the current operand
            for i in range(index, len(num)):
                # Avoid operands with leading zeros (e.g., "05" is invalid, but "0" is valid)
                if i > index and num[index] == '0':
                    break
                    
                # Extract the current operand as a string and convert to integer
                current_str = num[index : i + 1]
                current_num = int(current_str)
                
                if index == 0:
                    # If this is the first operand, we just start the expression with it
                    backtrack(i + 1, current_num, current_num, current_str)
                else:
                    # Option 1: Addition
                    backtrack(i + 1, current_num, current_value + current_num, expression + "+" + current_str)
                    
                    # Option 2: Subtraction
                    backtrack(i + 1, -current_num, current_value - current_num, expression + "-" + current_str)
                    
                    # Option 3: Multiplication
                    # To handle precedence, we subtract the previous operand from the current value,
                    # then add the product of the previous operand and the current operand.
                    backtrack(i + 1, prev_operand * current_num, (current_value - prev_operand) + (prev_operand * current_num), expression + "*" + current_str)
                    
        backtrack(0, 0, 0, "")
        return result