class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        # dp[x] = max length of consecutive sequence ending at x
        dp = {}
        max_len = 0
        
        for num in nums:
            # We must read the current dp values BEFORE updating them.
            # This ensures we don't accidentally use the current 'num' twice.
            len_keep = dp.get(num - 1, 0) + 1
            len_inc = dp.get(num, 0) + 1
            
            # Update the dp table
            dp[num] = max(dp.get(num, 0), len_keep)
            dp[num + 1] = max(dp.get(num + 1, 0), len_inc)
            
            # Update the maximum length found so far
            max_len = max(max_len, dp[num], dp[num + 1])
            
        return max_len