class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid + 1]:
                # We are on an ascending slope, so a peak is to the right
                left = mid + 1
            else:
                # We are on a descending slope, so a peak is at mid or to the left
                right = mid
                
        # When left == right, we have found a peak
        return left