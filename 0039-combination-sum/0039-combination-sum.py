class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(remain: int, combo: List[int], start: int):
            # Base case: If the remaining target is 0, we found a valid combination
            if remain == 0:
                result.append(list(combo))
                return
            # If the remaining target is negative, we overshot, so stop exploring
            elif remain < 0:
                return
            
            # Iterate through the candidates starting from 'start' index
            for i in range(start, len(candidates)):
                # Add the current candidate to our combination
                combo.append(candidates[i])
                
                # Recursively call backtrack with the updated remaining sum.
                # We pass 'i' (not 'i + 1') because we can reuse the same number.
                backtrack(remain - candidates[i], combo, i)
                
                # Backtrack: remove the last added candidate before moving to the next one
                combo.pop()
                
        # Start the backtracking process
        backtrack(target, [], 0)
        
        return result