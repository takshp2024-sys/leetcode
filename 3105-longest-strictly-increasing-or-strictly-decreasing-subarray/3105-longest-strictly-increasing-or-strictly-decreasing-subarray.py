class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        max_len = 1
        inc_len = 1
        dec_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # Strictly increasing
                inc_len += 1
                dec_len = 1
            elif nums[i] < nums[i - 1]:
                # Strictly decreasing
                dec_len += 1
                inc_len = 1
            else:
                # Equal elements break both sequences
                inc_len = 1
                dec_len = 1
                
            # Update the maximum length found so far
            max_len = max(max_len, inc_len, dec_len)
            
        return max_len