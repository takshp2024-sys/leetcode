class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to easily skip duplicates
        nums.sort()
        result = []
        used = [False] * len(nums)
        
        def backtrack(current_permutation: List[int]):
            # Base case: If the permutation is full, add it to the result
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return
            
            # Iterate through the available numbers
            for i in range(len(nums)):
                # Skip if the number is already used in the current path
                if used[i]:
                    continue
                    
                # Skip duplicates: If the current number is the same as the previous 
                # AND the previous was not used in this path, skipping it avoids duplicate branches.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                    
                # Choose the number
                used[i] = True
                current_permutation.append(nums[i])
                
                # Recurse
                backtrack(current_permutation)
                
                # Undo the choice (backtrack)
                used[i] = False
                current_permutation.pop()
                
        backtrack([])
        return result