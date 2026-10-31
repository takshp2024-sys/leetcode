class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # If we found the target, return its index
            if nums[mid] == target:
                return mid
                
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # If the target is within the sorted left half, search left
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # Otherwise, search the right half
                    left = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # If the target is within the sorted right half, search right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # Otherwise, search the left half
                    right = mid - 1
                    
        return -1