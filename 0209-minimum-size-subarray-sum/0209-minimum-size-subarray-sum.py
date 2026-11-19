class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            # Expand the window by adding the right element
            current_sum += nums[right]
            
            # Shrink the window from the left as long as the sum meets the target
            while current_sum >= target:
                # Update the minimum length found so far
                min_length = min(min_length, right - left + 1)
                # Remove the left element and move the left pointer
                current_sum -= nums[left]
                left += 1
                
        # If min_length was never updated, no valid subarray exists
        return min_length if min_length != float('inf') else 0