class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Place each number in its "correct" index if possible.
        # A number 'x' (where 1 <= x <= n) belongs at index 'x - 1'.
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its correct position
                # Note: We must be careful with the order of assignment 
                # to avoid overwriting values prematurely.
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Find the first index that doesn't have the correct number.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: If all numbers 1 through n are present, the answer is n + 1.
        return n + 1