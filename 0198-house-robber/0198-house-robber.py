class Solution:
    def rob(self, nums: List[int]) -> int:
        # prev2 represents the max profit up to house i-2
        # prev1 represents the max profit up to house i-1
        prev2 = 0
        prev1 = 0
        
        for num in nums:
            # The max profit for the current house is either:
            # 1. Skip current house: prev1
            # 2. Rob current house: prev2 + num
            current_max = max(prev1, prev2 + num)
            
            # Shift the variables for the next iteration
            prev2 = prev1
            prev1 = current_max
            
        return prev1