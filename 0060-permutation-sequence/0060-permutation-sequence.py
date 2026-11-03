import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of available numbers from 1 to n
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Precompute factorials for 0! to (n-1)!
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
            
        # We use 0-based indexing for k to make the math easier
        k -= 1
        
        result = []
        
        # Build the permutation digit by digit
        for i in range(n - 1, -1, -1):
            # Determine which number to pick from the remaining 'numbers' list
            index = k // fact[i]
            
            # Append the chosen number to the result
            result.append(numbers.pop(index))
            
            # Update k for the next position
            k %= fact[i]
            
        return "".join(result)