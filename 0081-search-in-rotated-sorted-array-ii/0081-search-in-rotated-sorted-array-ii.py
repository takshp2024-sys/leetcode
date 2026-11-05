class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
                
            # The tricky part: If left, mid, and right are all the same, 
            # we can't determine which side is sorted.
            # We just shrink the boundaries by 1 and try again.
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                
            # Check if the left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Otherwise, the right half must be sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False