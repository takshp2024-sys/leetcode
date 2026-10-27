class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to use the two-pointer approach
        nums.sort()
        
        # Initialize the closest sum with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            # We can skip duplicate values for the first element to optimize
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find an exact match, it's the closest possible sum
                if current_sum == target:
                    return current_sum
                
                # Update the closest_sum if the current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers to adjust the sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum