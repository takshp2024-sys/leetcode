class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    # Keep searching to the left to find the absolute first occurrence
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid
                    # Keep searching to the right to find the absolute last occurrence
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        # Call the two binary searches
        return [find_first(nums, target), find_last(nums, target)]