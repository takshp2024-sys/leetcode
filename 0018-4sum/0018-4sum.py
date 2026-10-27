class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        # First loop for the first number
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Second loop for the second number
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        # Move both pointers inward
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res