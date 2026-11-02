class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our tracking variables with the first element
        current_sum = nums[0]
        max_sum = nums[0]
        
        # Iterate through the rest of the array
        for i in range(1, len(nums)):
            # If current_sum is negative, it drags down the next sum.
            # So, we either start a new subarray here, or add to the existing one.
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the maximum sum seen so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum