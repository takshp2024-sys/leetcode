class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # We have 4 options to minimize the range after changing 2 elements:
        # 1. Change the two smallest elements: range is nums[n-1] - nums[2]
        # 2. Change the smallest and the second smallest: range is nums[n-1] - nums[2] (covered by 1)
        # 3. Change the two largest elements: range is nums[n-3] - nums[0]
        # 4. Change the largest and the second largest: range is nums[n-3] - nums[0] (covered by 3)
        # 5. Change the smallest and the largest: range is nums[n-2] - nums[1]
        
        # Actually, the standard 3 choices are:
        # - Change the two largest: nums[n-3] - nums[0]
        # - Change the two smallest: nums[n-1] - nums[2]
        # - Change the smallest and the largest: nums[n-2] - nums[1]
        
        return min(
            nums[n-1] - nums[2],
            nums[n-3] - nums[0],
            nums[n-2] - nums[1]
        )