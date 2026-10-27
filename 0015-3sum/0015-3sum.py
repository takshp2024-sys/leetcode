class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array to use two pointers and easily skip duplicates
        
        for i in range(len(nums)):
            # If the current number is greater than 0, the sum of it 
            # and any subsequent numbers will be > 0, so we can break early.
            if nums[i] > 0:
                break
                
            # Skip duplicate elements for the first number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer right
                elif current_sum > 0:
                    right -= 1 # We need a smaller sum, move right pointer left
                else:
                    # We found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers inward
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res