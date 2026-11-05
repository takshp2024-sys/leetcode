class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(index: int, current_subset: List[int]):
            # Add the current subset to our result list.
            # We add a copy because 'current_subset' will be modified in-place during backtracking.
            result.append(list(current_subset))
            
            # Iterate through the remaining numbers
            for i in range(index, len(nums)):
                # Include nums[i] in the current subset
                current_subset.append(nums[i])
                
                # Recurse to build further subsets
                backtrack(i + 1, current_subset)
                
                # Backtrack: remove nums[i] to explore the branch where it is excluded
                current_subset.pop()
                
        backtrack(0, [])
        return result