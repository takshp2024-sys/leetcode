class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to handle duplicates and make skipping easier
        candidates.sort()
        result = []
        
        def backtrack(remain: int, combo: List[int], start: int):
            # Base case: exact target reached
            if remain == 0:
                result.append(list(combo))
                return
            
            # Iterate through the candidates starting from 'start' index
            for i in range(start, len(candidates)):
                # Optimization: If the current number is greater than the remaining target, 
                # the subsequent numbers will also be too large (since it's sorted).
                if candidates[i] > remain:
                    break
                
                # Skip duplicates: If this is not the first element in the current loop 
                # and it's the same as the previous element, skip it to avoid duplicate combinations.
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include the current candidate
                combo.append(candidates[i])
                
                # Recursively call backtrack with 'i + 1' because each number can only be used once
                backtrack(remain - candidates[i], combo, i + 1)
                
                # Backtrack: remove the last added candidate
                combo.pop()
                
        backtrack(target, [], 0)
        return result