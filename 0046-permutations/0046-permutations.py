class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(current_permutation: List[int]):
            # Base case: If the current permutation has the same length as nums,
            # we have formed a complete permutation.
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return
            
            # Iterate through all numbers in nums
            for num in nums:
                # If the number is not already in the current permutation, add it
                if num not in current_permutation:
                    current_permutation.append(num)
                    
                    # Recursively build the rest of the permutation
                    backtrack(current_permutation)
                    
                    # Backtrack: remove the last added number to try the next possibility
                    current_permutation.pop()
                    
        backtrack([])
        return result