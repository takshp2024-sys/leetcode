class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to bring duplicates together
        nums.sort()
        result = []
        
        def backtrack(start: int, current_subset: List[int]):
            # Add the current subset to the result (make a copy)
            result.append(list(current_subset))
            
            # Iterate through the remaining elements
            for i in range(start, len(nums)):
                # Skip duplicates: If the current element is the same as the previous one,
                # and the previous one was not included in the current subset, skip it.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                    
                # Include the current element
                current_subset.append(nums[i])
                
                # Recurse
                backtrack(i + 1, current_subset)
                
                # Backtrack (remove the element)
                current_subset.pop()
                
        backtrack(0, [])
        return result