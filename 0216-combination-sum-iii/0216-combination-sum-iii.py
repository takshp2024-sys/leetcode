class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current_combo: List[int], current_sum: int):
            # Base case: if we have exactly k numbers
            if len(current_combo) == k:
                if current_sum == n:
                    result.append(list(current_combo))
                return
            
            # Optimization: if the current sum exceeds n, stop exploring this path
            if current_sum > n:
                return
                
            # Iterate through possible next numbers
            # We can stop early if we don't have enough numbers left to reach k
            for num in range(start, 10):
                current_combo.append(num)
                backtrack(num + 1, current_combo, current_sum + num)
                current_combo.pop()  # Backtrack
                
        backtrack(1, [], 0)
        return result