class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # The minimum is strictly in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # The minimum is in the left half (including mid)
                right = mid
            else:
                # nums[mid] == nums[right]
                # We can't determine which side the minimum is on, 
                # so we safely reduce the search space by moving the right pointer.
                right -= 1
                
        return nums[left]