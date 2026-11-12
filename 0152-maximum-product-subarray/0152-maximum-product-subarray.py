class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Initialize the maximum and minimum products ending at the first element
        max_so_far = nums[0]
        min_so_far = nums[0]
        
        # The global maximum product
        result = max_so_far
        
        for i in range(1, len(nums)):
            current = nums[i]
            
            # If the current number is negative, the max product becomes the min product
            # and the min product becomes the max product when multiplied by 'current'.
            # To handle this without extra if-conditions, we calculate both possibilities.
            
            temp_max = max(current, max_so_far * current, min_so_far * current)
            min_so_far = min(current, max_so_far * current, min_so_far * current)
            
            # Update max_so_far for the next iteration
            max_so_far = temp_max
            
            # Update the global result
            result = max(result, max_so_far)
            
        return result