class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge cases for 1 or 2 houses
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        # Helper function to solve the linear House Robber problem
        def rob_linear(houses: List[int]) -> int:
            prev2 = 0
            prev1 = 0
            
            for num in houses:
                current_max = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = current_max
                
            return prev1
            
        # Case 1: Rob houses 0 to n-2 (exclude last)
        max1 = rob_linear(nums[:-1])
        # Case 2: Rob houses 1 to n-1 (exclude first)
        max2 = rob_linear(nums[1:])
        
        return max(max1, max2)