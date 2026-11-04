class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointers for the boundaries of 0s, current element, and 2s
        left = 0               # Everything before 'left' is 0
        right = len(nums) - 1  # Everything after 'right' is 2
        current = 0            # Pointer to the current element being processed
        
        while current <= right:
            if nums[current] == 0:
                # Swap current 0 to the left section
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                # Swap current 2 to the right section
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
                # Note: We don't increment 'current' here because the swapped
                # element from the right hasn't been processed yet.
            else:
                # It's a 1, so it's already in the correct middle section
                current += 1