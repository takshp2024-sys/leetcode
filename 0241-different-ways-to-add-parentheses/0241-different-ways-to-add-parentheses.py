class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        
        def compute(expr: str) -> List[int]:
            # If the result for this expression is already computed, return it
            if expr in memo:
                return memo[expr]
                
            # Base case: If the string has no operators, it's just a number
            if expr.isdigit():
                return [int(expr)]
                
            results = []
            
            # Iterate through the expression to find operators
            for i, char in enumerate(expr):
                if char in "+-*":
                    # Recursively compute all possible results for the left and right parts
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    # Combine the results from left and right using the current operator
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)
                                
            # Save the result in the memo dictionary
            memo[expr] = results
            return results
            
        return compute(expression)