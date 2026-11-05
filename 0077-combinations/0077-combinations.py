class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current_combo: List[int]):
            # Base case: If the combination has k numbers, add it to the result
            if len(current_combo) == k:
                result.append(list(current_combo))
                return
            
            # Calculate the maximum number we can pick to leave enough numbers remaining
            # to complete a combination of size k.
            # If we need (k - len(current_combo)) more numbers, we must stop at 
            # n - (k - len(current_combo)) + 1.
            max_val = n - (k - len(current_combo)) + 1
            
            for i in range(start, max_val + 1):
                # Add the current number
                current_combo.append(i)
                # Recurse to pick the next number (starting from i + 1 to avoid duplicates)
                backtrack(i + 1, current_combo)
                # Backtrack: remove the last added number
                current_combo.pop()
                
        backtrack(1, [])
        return result